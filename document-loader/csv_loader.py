from pathlib import Path
from langchain_community.document_loaders import CSVLoader

BASE_DIR = Path(__file__).resolve().parent
loader = CSVLoader(file_path=str(BASE_DIR / 'Social_Network_Ads.csv'))

docs = loader.load()

print(len(docs))
print(docs[1])