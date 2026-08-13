text = """
RAG stands for Retrieval-Augmented Generation.
RAG retrieves relevant information.
The retrieved information is given to an LLM.
The LLM generates the final answer.
"""

chunk_size = 50

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

for chunk in chunks:
    print("CHUNK:")
    print(chunk)
    print()