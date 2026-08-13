from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "RAG helps AI retrieve relevant information."

embedding = model.encode(text)

print(embedding)
print("Dimensions:", len(embedding))