text = """
RAG stands for Retrieval-Augmented Generation.
RAG retrieves relevant information before generating an answer.
The retrieved information is given to an LLM.
The LLM generates the final answer.
"""

chunk_size = 60
overlap = 10

chunks = []

start = 0

while start < len(text):

    end = start + chunk_size

    chunk = text[start:end]

    chunks.append(chunk)

    start = end - overlap


for chunk in chunks:

    print("CHUNK:")
    print(chunk)
    print()