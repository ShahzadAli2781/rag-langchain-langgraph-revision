import chromadb
from langchain_huggingface import HuggingFaceEmbeddings


# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="rag_documents"
)


# Documents
documents = [
    "Python is a programming language.",
    "RAG retrieves relevant information before generating an answer.",
    "ChromaDB is a vector database.",
    "LangChain is a framework for building LLM applications."
]


# Create embeddings
vectors = embeddings.embed_documents(documents)


# Store documents + embeddings
collection.add(
    documents=documents,
    embeddings=vectors,
    ids=["1", "2", "3", "4"]
)


# User question
query = "What is a vector database?"


# Query embedding
query_vector = embeddings.embed_query(query)


# Search
results = collection.query(
    query_embeddings=[query_vector],
    n_results=2
)


print("Question:")
print(query)

print("\nRelevant Documents:")
print(results["documents"])