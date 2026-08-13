import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()


documents = [
    "Python is a high-level programming language.",
    "RAG stands for Retrieval-Augmented Generation.",
    "RAG allows an AI system to retrieve relevant information before generating an answer.",
    "LangChain is a framework for building applications powered by language models.",
    "ChromaDB is a vector database commonly used for storing and searching embeddings."
]


query = "What is ChromaDB?"



# Retrieval


query_words = query.lower().replace("?", "").split()

retrieved_documents = []


for document in documents:

    document_words = document.lower().split()

    for word in query_words:

        if word in document_words:
            retrieved_documents.append(document)
            break



# Context


context = "\n".join(retrieved_documents)



# LLM


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{query}
"""


response = llm.invoke(prompt)


answer = response.content


print("Question:")
print(query)

print("\nRetrieved Context:")
print(context)

print("\nAnswer:")
print(answer)