from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
RAG stands for Retrieval-Augmented Generation.
RAG retrieves relevant information before generating an answer.
The retrieved information is given to an LLM.
The LLM generates the final answer.
"""


splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)


chunks = splitter.split_text(text)


for chunk in chunks:
    print("CHUNK:")
    print(chunk)
    print()