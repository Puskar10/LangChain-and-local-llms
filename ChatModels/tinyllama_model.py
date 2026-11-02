
import torch
from pathlib import Path

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

from langchain_huggingface import HuggingFacePipeline


# Automatically find the model folder
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "TinyLlama"


def load_tinyllama():

    # Check model availability
    if not (MODEL_PATH / "config.json").exists():
        raise FileNotFoundError(
            f"TinyLlama model not found at: {MODEL_PATH}"
        )

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        str(MODEL_PATH),
        local_files_only=True
    )

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        str(MODEL_PATH),
        torch_dtype=torch.float32,
        local_files_only=True
    )

    # Avoid conflicting generation length settings
    model.generation_config.max_length = None

    # Create text generation pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        return_full_text=False
    )

    # Connect with LangChain
    llm = HuggingFacePipeline(
        pipeline=pipe
    )

    return llm
