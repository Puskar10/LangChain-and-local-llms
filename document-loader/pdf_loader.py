from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

BASE_DIR = Path(__file__).resolve().parent

file_path = BASE_DIR / "Chapter_1_Strategic_Management_Complete_Study_Notes.pdf"

Loader = PyPDFLoader(str(file_path))




docs = Loader.load()
print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)