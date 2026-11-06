from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

prompt = PromptTemplate(
    template="Write a Short Story about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()
chain = prompt | llm | parser

result = chain.invoke({'topic': 'A Brave Little Toaster'})

print(result)

chain.get_graph().print_ascii()