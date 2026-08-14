from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("sample.pdf")

documents = loader.load()


print("Total Pages:", len(documents))

print("\nFirst Page:")
print(documents[0].page_content)

print("\nMetadata:")
print(documents[0].metadata)