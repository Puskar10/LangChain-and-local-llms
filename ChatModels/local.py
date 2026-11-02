from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# Store Hugging Face downloaded models on D:
os.environ["HF_HOME"] = r"D:\huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
    },
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")

print(result.content)

