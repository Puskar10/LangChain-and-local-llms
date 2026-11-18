from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda
)
from langchain_core.output_parsers import StrOutputParser


# ==========================================
# 1. YouTube Transcript
# ==========================================

video_id = "Gfr50f6ZBvo"

api = YouTubeTranscriptApi()
fetched_transcript = api.fetch(video_id, languages=["en"])

transcript = " ".join(
    snippet.text for snippet in fetched_transcript
)

print("Transcript fetched successfully!")


# ==========================================
# 2. Text Splitting
# ==========================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.create_documents(
    [transcript],
    metadatas=[{"video_id": video_id}]
)

print(f"Total chunks: {len(chunks)}")


# ==========================================
# 3. Embeddings
# ==========================================

embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)


# ==========================================
# 4. Vector Store
# ==========================================

vector_store = Chroma(
    collection_name="yt_video_summarizer",
    embedding_function=embedding,
    persist_directory="./chroma_db"
)

# Remove old documents belonging to this video
existing = vector_store.get(
    where={"video_id": video_id}
)

if existing["ids"]:
    vector_store.delete(ids=existing["ids"])


# Add chunks
vector_store.add_documents(
    documents=chunks,
    ids=[f"{video_id}_{i}" for i in range(len(chunks))]
)

print("Documents stored in ChromaDB!")


# ==========================================
# 5. Retriever
# ==========================================

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)


# ==========================================
# 6. LLM
# ==========================================

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.2
)


# ==========================================
# 7. Prompt
# ==========================================

prompt = PromptTemplate(
    template="""
You are a helpful assistant answering questions about a YouTube video.

Answer ONLY from the provided transcript context.
If the context is insufficient, say:
"I don't know based on this transcript."

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)


# ==========================================
# 8. Format Documents
# ==========================================

def format_docs(docs):
    return "\n\n".join(
        doc.page_content for doc in docs
    )


# ==========================================
# 9. LCEL Chain
# ==========================================

chain = (
    RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })
    | prompt
    | llm
    | StrOutputParser()
)


# ==========================================
# 10. Ask Question
# ==========================================

question = """
Is nuclear fusion discussed in this video?
If yes, what was discussed?
"""

answer = chain.invoke(question)

print("\nAnswer:")
print(answer)