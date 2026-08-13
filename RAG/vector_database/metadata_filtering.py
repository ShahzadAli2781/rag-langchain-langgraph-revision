import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="metadata_practice"
)

collection.add(
    documents=[
        "RAG retrieves relevant information before generating an answer.",
        "Python is a programming language.",
        "ChromaDB is a vector database.",
        "LangChain helps developers build LLM applications."
    ],
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4"
    ],
    metadatas=[
        {"topic": "rag"},
        {"topic": "python"},
        {"topic": "database"},
        {"topic": "langchain"}
    ]
)

results = collection.query(
    query_texts=["What is RAG?"],
    n_results=2,
    where={"topic": "rag"}
)

print(results["documents"])