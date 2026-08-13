from langchain_core.documents import Document


documents = [
    Document(
        page_content="RAG retrieves relevant information before generating an answer.",
        metadata={
            "source": "rag_notes.pdf",
            "page": 1,
            "topic": "RAG"
        }
    ),

    Document(
        page_content="ChromaDB is a vector database.",
        metadata={
            "source": "vector_notes.pdf",
            "page": 2,
            "topic": "Vector Database"
        }
    )
]


for document in documents:

    print("CONTENT:")
    print(document.page_content)

    print("METADATA:")
    print(document.metadata)

    print()