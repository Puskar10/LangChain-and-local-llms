
from huggingface_hub import snapshot_download
from pathlib import Path

# Hugging Face model
MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Automatically create the model directory
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "TinyLlama"

MODEL_PATH.mkdir(parents=True, exist_ok=True)

print("Starting TinyLlama download...")
print(f"Download location: {MODEL_PATH}")

snapshot_download(
    repo_id=MODEL_ID,
    local_dir=str(MODEL_PATH)
)

print("\nDownload completed successfully!")
print("Config exists:", (MODEL_PATH / "config.json").exists())
