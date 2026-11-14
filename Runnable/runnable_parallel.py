from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel

model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

prompt1 = PromptTemplate(
    template= 'Generate a tweet about {topic}',
    input_variable=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel ({
    'tweet': RunnableSequence(prompt1 , model , parser),
    'linkedin': RunnableSequence(prompt2 , model , parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print(result['linkedin'])