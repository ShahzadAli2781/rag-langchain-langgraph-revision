from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


documents = [
    "RAG retrieves relevant information before generating an answer.",
    "Python is a popular programming language.",
    "ChromaDB is a vector database.",
    "LangChain helps developers build LLM applications."
]


query = "How does RAG find information?"


query_vector = model.encode([query])
document_vectors = model.encode(documents)


scores = cosine_similarity(query_vector, document_vectors)[0]


best_index = scores.argmax()


print("Query:", query)
print("Best Document:", documents[best_index])
print("Similarity:", scores[best_index])