from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq


load_dotenv()


# 1. Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()


# 2. Split PDF into chunks
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
    collection_name="complete_rag"
)


# 5. Create Retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)


# 6. User question
question = "What is SkillForge AI?"


# 7. Retrieve relevant chunks
results = retriever.invoke(question)


# 8. Create context
context = "\n\n".join(
    document.page_content
    for document in results
)


# 9. LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# 10. Prompt
prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{question}
"""


# 11. Generate answer
response = llm.invoke(prompt)


print("QUESTION:")
print(question)

print("\nANSWER:")
print(response.content)