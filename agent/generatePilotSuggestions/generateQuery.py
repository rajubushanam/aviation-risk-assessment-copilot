from openai import OpenAI
from pinecone import Pinecone
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
index = pc.Index(name='pilot-handbook')
def query_pinecone(question):
    """Query Pinecone for the most relevant chunks."""
    question_embedding = client.embeddings.create(
        input=question,
        model="text-embedding-ada-002"
    ).data[0].embedding

    results = index.query(
        vector=question_embedding,
        top_k=5,  # Number of relevant chunks to retrieve
        include_metadata=True
    )
    print(results)
    return results.matches