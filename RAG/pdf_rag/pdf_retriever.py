from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# 1. Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()


# 2. Create chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)


# 3. Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 4. Store in ChromaDB
vector_store = Chroma.from_documents(
    chunks,
    embedding=embeddings,
    collection_name="pdf_rag"
)


# 5. Create Retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)


# 6. Ask question
question = "What is RAG?"

results = retriever.invoke(question)


# 7. Show results
for document in results:
    print("RELEVANT CHUNK:")
    print(document.page_content)

    print("\nMETADATA:")
    print(document.metadata)

    print("-" * 50)