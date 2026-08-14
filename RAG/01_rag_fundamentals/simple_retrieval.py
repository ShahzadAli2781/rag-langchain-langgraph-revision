documents = [
    "Python is a high-level programming language.",
    "RAG stands for Retrieval-Augmented Generation.",
    "RAG allows an AI system to retrieve relevant information before generating an answer.",
    "LangChain is a framework for building applications powered by language models.",
    "ChromaDB is a vector database commonly used for storing and searching embeddings."
]

query = "What is RAG?"


query_words = query.lower().split()


results = []


for document in documents:

    document_words = document.lower().split()

    score = 0

    for word in query_words:
        if word in document_words:
            score += 1

    results.append((document, score))


results.sort(
    key=lambda x: x[1],
    reverse=True
)


print("Query:", query)

print("\nRetrieved Documents:\n")


for document, score in results:

    if score > 0:
        print(f"Score: {score}")
        print("Document:", document)
        print()