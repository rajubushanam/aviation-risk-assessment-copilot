from pinecone import Pinecone, ServerlessSpec
from itertools import islice
import time
import os

pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

# Create or connect to an index
index_name = "pilot-handbook"
print(pc.list_indexes())
if any(index.name == index_name for index in pc.list_indexes()):
    print('Index already exists')
else:
    pc.create_index(name=index_name, dimension=1536, spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            ))  # Dimension of ADA embeddings
index = pc.Index(name=index_name)

def get_data_upload_to_pinecone(embeddings, chunks):
    """Store embeddings and chunks in Pinecone."""
    data = []
    for i, embedding in enumerate(embeddings):
        data.append(
            (f"chunk-{i}", embedding, {"text": chunks[i]})
        )
    return data

def safe_batch_upsert(embeddings, chunks, batch_size=50, retries=3):
    data = get_data_upload_to_pinecone(embeddings=embeddings, chunks=chunks)
    """Upsert data into Pinecone in batches with retries."""
    it = iter(data)
    while batch := list(islice(it, batch_size)):
        for attempt in range(retries):
            try:
                index.upsert(vectors=batch)
                print(f"Batch of size {len(batch)} uploaded successfully.")
                break
            except Exception as e:
                print(f"Error during upsert: {e}")
                if attempt < retries - 1:
                    time.sleep(2)  # Retry after a short delay
                else:
                    print("Failed after multiple retries.")