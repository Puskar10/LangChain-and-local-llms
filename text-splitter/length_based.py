from pathlib import Path
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader



BASE_DIR = Path(__file__).resolve().parent
loader = PyPDFLoader(file_path=str(BASE_DIR / 'dl-curriculum.pdf'))

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)
print(len(result))