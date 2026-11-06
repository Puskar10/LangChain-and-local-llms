from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

# Define the local model
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

class Person(BaseModel):
    name: str = Field(description='Name of the person'),
    age: int = Field(gt=18, description='Age of the person'),
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | llm | parser

final_output = chain.invoke({'place': 'New York'})
print(final_output.name)