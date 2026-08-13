import chromadb

client = chromadb.Client()

collection = client.create_collection("rag_practice")

collection.add(
    documents=[
        "RAG retrieves relevant information before generating an answer.",
        "Python is a programming language.",
        "ChromaDB is a vector database.",
        "LangChain helps build LLM applications."
    ],
    ids=["doc1", "doc2", "doc3", "doc4"]
)

results = collection.query(
    query_texts=["How does RAG retrieve information?"],
    n_results=2
)

print(results["documents"])