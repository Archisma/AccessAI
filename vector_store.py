import os
from pathlib import Path

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# Where we persist the vector DB
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CHROMA_DIR = BASE_DIR / "chroma_db"

SUBJECT_FILES = {
    "math": DATA_DIR / "math.txt",
    "english": DATA_DIR / "english.txt",
    "cognitive": DATA_DIR / "cognitive.txt",
    "gk": DATA_DIR / "gk.txt",
}

def build_or_load_vectorstore():
    """
    Builds a Chroma vector database from /data/*.txt if not already present.
    Uses metadata facets (subject) so we can filter retrieval by dropdown mode.
    """
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


    # If a Chroma collection already exists, load it.
    if any(CHROMA_DIR.iterdir()):
        return Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=embeddings
        )

    # Otherwise, build it from scratch.
    texts = []
    metadatas = []

    splitter = RecursiveCharacterTextSplitter(chunk_size=350, chunk_overlap=50)

    for subject, filepath in SUBJECT_FILES.items():
        if not filepath.exists():
            raise FileNotFoundError(f"Missing data file: {filepath}")

        content = filepath.read_text(encoding="utf-8").strip()
        if not content:
            continue

        chunks = splitter.split_text(content)
        for chunk in chunks:
            texts.append(chunk)
            # Facet metadata (important!)
            metadatas.append({
                "subject": subject,
                "source_file": filepath.name
            })

    vectorstore = Chroma.from_texts(
        texts=texts,
        metadatas=metadatas,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name="accessai_adhd"
    )
    vectorstore.persist()
    return vectorstore
