from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

text1 = "RAG retrieves information for an AI."
text2 = "RAG finds useful information before answering."
text3 = "The weather is very cold today."

vector1 = model.encode([text1])
vector2 = model.encode([text2])
vector3 = model.encode([text3])



print("RAG vs RAG:", cosine_similarity(vector1, vector2)[0][0])
print("RAG vs Weather:", cosine_similarity(vector1, vector3)[0][0])