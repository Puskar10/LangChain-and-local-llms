
import torch
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = Path("models/TinyLlama")

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    str(MODEL_PATH),
    local_files_only=True
)

print("Loading model...")

model = AutoModelForCausalLM.from_pretrained(
    str(MODEL_PATH),
    dtype=torch.float32,
    local_files_only=True
)

model.eval()

# TinyLlama chat format
messages = [
    {
        "role": "user",
        "content": "Explain what a black hole is in simple words."
    }
]

# Tokenize prompt
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True
)

print("Input tokens:", inputs["input_ids"].shape)

# Generate response
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id
    )

# Extract generated tokens
input_length = inputs["input_ids"].shape[-1]
new_tokens = outputs[0][input_length:]

print("Generated token IDs:", new_tokens.tolist())

response = tokenizer.decode(
    new_tokens,
    skip_special_tokens=True
)

print("\n========== TINYLLAMA RESPONSE ==========")
print(repr(response))
