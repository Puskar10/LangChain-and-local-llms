
import streamlit as st
import torch

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Hugging Face model ID
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Load model
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

# Create text generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.7,
    do_sample=True,
    return_full_text=False
)

# Connect with LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Streamlit UI
st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# Prompt template
template = PromptTemplate(
    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ],
    template="""
<|system|>
You are a helpful research paper explanation assistant.
Explain concepts clearly and accurately.
</s>
<|user|>
Explain the research paper: {paper_input}

Explanation style: {style_input}
Explanation length: {length_input}

Include:
1. Introduction
2. Main concept
3. Methodology
4. Important findings
5. Applications
</s>
<|assistant|>
"""
)

# Create chain
parser = StrOutputParser()
chain = template | llm | parser

# Generate response
if st.button("Generate Explanation"):

    with st.spinner("TinyLlama is thinking..."):

        response = chain.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })

        st.subheader("Research Paper Explanation")
        st.write(response)
