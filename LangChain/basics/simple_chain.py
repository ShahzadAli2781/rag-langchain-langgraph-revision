from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)


chain = prompt | llm


response = chain.invoke({
    "topic": "Agentic AI"
})


print(response.content)