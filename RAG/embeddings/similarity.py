from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

text1 = "RAG retrieves information for an AI."
text2 = "RAG finds useful information before answering."

vector1 = model.encode([text1])
vector2 = model.encode([text2])

score = cosine_similarity(vector1, vector2)

print("Similarity:", score[0][0])