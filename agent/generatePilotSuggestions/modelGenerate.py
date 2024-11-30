import pandas as pd
import os
from .extractTextFromPDF import extract_text_from_pdf
from .chunkText import chunk_text
from .generateEmbeddings import generate_embeddings
from .storeChunksEmbeddings import safe_batch_upsert

script_path = os.path.abspath(__file__)
project_path = os.path.dirname(script_path)
# make sure the file name matches below name and path matches this file location
filePath = project_path + "/faa-pilot.pdf"
if not os.path.exists(filePath):
    raise FileNotFoundError(f"No such file: '{filePath}'")

def load_model_input():
    # Extract text from your pilot handbook PDF
    pdf_text = extract_text_from_pdf(filePath)

    # Save to a file (optional for debugging)
    with open(project_path + "/faa_pilot.txt", "w", encoding="utf-8") as file:
        file.write(pdf_text)

        # Chunk the extracted text
    text_chunks = chunk_text(pdf_text, chunk_size=500)

    # Display the first few chunks for debugging
    for i, chunk in enumerate(text_chunks[:3], start=1):
        print(f"Chunk {i}:\n{chunk}\n")

    # Generate embeddings for the text chunks
    chunk_embeddings = generate_embeddings(text_chunks)
    print(len(chunk_embeddings))

    # Perform batch upload
    safe_batch_upsert(embeddings=chunk_embeddings,chunks=text_chunks)
    # upsert_embeddings_to_pinecone(chunk_embeddings, text_chunks)
    