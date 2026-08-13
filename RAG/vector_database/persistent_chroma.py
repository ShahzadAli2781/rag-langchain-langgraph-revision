import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="rag_practice"
)


collection.add(
    documents=[
        "RAG retrieves relevant information before generating an answer.",
        "Python is a programming language.",
        "ChromaDB is a vector database.",
        "LangChain helps developers build LLM applications.",
        "Embeddings convert text into numerical vectors."
    ],
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4",
        "doc5"
    ]
)


results = collection.query(
    query_texts=["How does RAG find relevant information?"],
    n_results=2
)


print("Top 2 Results:")
print(results["documents"])