from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = PyPDFLoader("sample.pdf")

documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


chunks = splitter.split_documents(documents)


print("Total Chunks:", len(chunks))

print("\nFirst Chunk:")
print(chunks[0].page_content)

print("\nMetadata:")
print(chunks[0].metadata)