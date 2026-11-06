
import torch
from pathlib import Path

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

from langchain_huggingface import HuggingFacePipeline

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "TinyLlama"


def load_tinyllama():

    if not (MODEL_PATH / "config.json").exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    print("Loading TinyLlama...")

    tokenizer = AutoTokenizer.from_pretrained(
        str(MODEL_PATH),
        local_files_only=True
    )

    model = AutoModelForCausalLM.from_pretrained(
        str(MODEL_PATH),
        dtype=torch.float32,
        local_files_only=True
    )

    model.eval()

    # Hugging Face pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        do_sample=False,
        return_full_text=False,
        pad_token_id=tokenizer.eos_token_id
    )

    # LangChain integration
    llm = HuggingFacePipeline(
        pipeline=pipe
    )

    print("TinyLlama ready!")

    return llm
