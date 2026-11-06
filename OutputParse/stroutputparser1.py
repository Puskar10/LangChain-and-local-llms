
from tinyllama_model import load_tinyllama

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = load_tinyllama()

# First prompt
template1 = PromptTemplate(
    template=(
        "<|system|>\n"
        "You are a helpful assistant. Write a detailed report on {topic}.\n"
        "<|assistant|>\n"
    ),
    input_variables=["topic"]
)

# Second prompt
template2 = PromptTemplate(
    template=(
        "<|system|>\n"
        "Summarize the following text in 5 lines:\n"
        "{text}\n"
        "<|assistant|>\n"
    ),
    input_variables=["text"]
)

parser = StrOutputParser()

chain = template1 | llm | parser | template2 | llm | parser

print("Generating report and summary...")

result = chain.invoke({
    "topic": "Black Holes"
})

print("\n========== FINAL SUMMARY ==========")
print(result)
