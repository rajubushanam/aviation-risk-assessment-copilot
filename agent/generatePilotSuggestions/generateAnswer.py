from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(question, context_chunks):
    """Generate an answer using GPT-4."""
    context = "\n".join(context_chunks)
    prompt = f"Answer the following question based on the provided context:\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text