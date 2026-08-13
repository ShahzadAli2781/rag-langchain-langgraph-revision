from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
RAG stands for Retrieval-Augmented Generation.
RAG retrieves relevant information before generating an answer.
The retrieved information is given to an LLM.
The LLM generates the final answer.
"""


document = Document(
    page_content=text,
    metadata={
        "source": "rag_notes.txt",
        "topic": "RAG"
    }
)


splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)


chunks = splitter.split_documents([document])


for chunk in chunks:

    print("CONTENT:")
    print(chunk.page_content)

    print("METADATA:")
    print(chunk.metadata)

    print()