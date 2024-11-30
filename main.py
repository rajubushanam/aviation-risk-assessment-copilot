from dotenv import load_dotenv, find_dotenv
import os
import sys

# Load environment variables from the .env file
loaded = load_dotenv(find_dotenv())

# Uncomment this to generate the data from pdf and store into vector DB
# from agent.generatePilotSuggestions.modelGenerate import load_model_input
# load_model_input()

# Access the command line arguments
filename = sys.argv[0]  # The script's name
user_question = sys.argv[1]  # First argument

from agent.generatePilotSuggestions.generateQuery import query_pinecone
# Example query
relevant_chunks = query_pinecone(user_question)
text_chunks=[]

print("Relevant Chunks:", relevant_chunks)
for chunk in relevant_chunks:
    print(chunk.metadata['text'])
    text_chunks.append(chunk.metadata['text'])

# Generate answer
from agent.generatePilotSuggestions.generateAnswer import generate_answer
answer = generate_answer(user_question, text_chunks)
print("Answer:", answer)

