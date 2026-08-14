from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


documents = [
    "RAG retrieves relevant information before generating an answer.",
    "ChromaDB is a vector database.",
    "Python is a programming language.",
    "LangChain is used to build LLM applications."
]

metadata = [
    {"topic": "RAG"},
    {"topic": "VectorDB"},
    {"topic": "Python"},
    {"topic": "LangChain"}
]


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vector_store = Chroma.from_texts(
    documents,
    embedding=embeddings,
    metadatas=metadata
)


results = vector_store.similarity_search(
    "What is RAG?",
    k=2,
    filter={"topic": "RAG"}
)


for document in results:
    print("RESULT:")
    print(document.page_content)

    print("METADATA:")
    print(document.metadata)

    print()