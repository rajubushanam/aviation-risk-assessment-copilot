from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_embeddings(chunks):
    """Generate embeddings for text chunks."""
    embeddings = []
    for chunk in chunks:
        response = client.embeddings.create(
            input=chunk,
            model="text-embedding-ada-002"
        )
        embeddings.append(response.data[0].embedding)
    return embeddings

