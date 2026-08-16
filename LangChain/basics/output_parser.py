from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one simple sentence."
)


parser = StrOutputParser()


chain = prompt | llm | parser


response = chain.invoke({
    "topic": "RAG"
})


print(response)