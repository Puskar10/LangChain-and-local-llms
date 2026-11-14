from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama




model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)


prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

BASE_DIR = Path(__file__).resolve().parent

# Locate cricket.txt
file_path = BASE_DIR / "cricket.txt"

loader = TextLoader(str(file_path), encoding="utf-8")

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))