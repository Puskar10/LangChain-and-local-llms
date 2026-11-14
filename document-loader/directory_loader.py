from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader



BASE_DIR = Path(__file__).resolve().parent
BOOKS_DIR = BASE_DIR / "books"

loader = DirectoryLoader(
    path=str(BOOKS_DIR),
    glob="*.pdf",
    loader_cls=PyPDFLoader,
    show_progress=True
)

docs = loader.lazy_load()

count = 0

for document in docs:
    count += 1

    print("\nPage:", document.metadata.get("page"))
    print("Source:", document.metadata.get("source"))
    print("Content:", document.page_content[:200])

print("\nTotal pages loaded:", count)