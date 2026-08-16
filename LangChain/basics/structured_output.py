from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel


load_dotenv()


class Topic(BaseModel):
    name: str
    description: str


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


structured_llm = llm.with_structured_output(Topic)


response = structured_llm.invoke(
    "Explain RAG in simple words."
)


print("Name:", response.name)
print("Description:", response.description)