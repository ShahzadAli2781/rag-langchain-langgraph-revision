import chromadb


client = chromadb.PersistentClient(path="./chroma_db")


collection = client.get_or_create_collection(
    name="rag_documents"
)


documents = [
    "RAG retrieves relevant information before generating an answer.",
    "ChromaDB is a vector database used for storing and searching embeddings."
]


collection.add(
    documents=documents,
    ids=["doc1", "doc2"]
)


print("Documents stored successfully.")

print("Total documents:", collection.count())