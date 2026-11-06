
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import (
    StructuredOutputParser,
    ResponseSchema
)

# Define the local model
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

# Define response schema
schema = [
    ResponseSchema(
        name="fact_1",
        description="Fact 1 about the topic"
    ),
    ResponseSchema(
        name="fact_2",
        description="Fact 2 about the topic"
    ),
    ResponseSchema(
        name="fact_3",
        description="Fact 3 about the topic"
    ),
]

# Create structured output parser
parser = StructuredOutputParser.from_response_schemas(schema)

# Create prompt template
template = PromptTemplate(
    template="""
Give exactly 3 facts about {topic}.

Return only valid JSON without markdown or extra explanation.

{format_instruction}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)

# Create chain
chain = template | llm | parser

# Invoke model
result = chain.invoke({
    "topic": "black hole"
})

# Display result
print("\nStructured Output:")
print(result)

print("\nIndividual Facts:")
print(result["fact_1"])
print(result["fact_2"])
print(result["fact_3"])
