
import streamlit as st
from pypdf import PdfReader
import re
from sentence_transformers import SentenceTransformer

st.set_page_config(
    page_title="RAG Document Q&A",
    page_icon="📚",
    layout="wide"
)

st.title("📚 RAG-Based Document Question Answering")
st.write("Upload a document and ask questions about its content.")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    all_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            all_text += text + "\n"

    st.success("Document uploaded successfully!")

    st.write("Number of pages:", len(reader.pages))

    # Clean text
    clean_text = re.sub(r'\s+', ' ', all_text).strip()

    # Create chunks
    words = clean_text.split()

    chunk_size = 500
    overlap = 50

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    st.write("Number of chunks:", len(chunks))

    # Create embeddings
    with st.spinner("Creating embeddings..."):

        embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        chunk_embeddings = embedding_model.encode(
            chunks,
            show_progress_bar=False
        )

    st.success("Embeddings created successfully!")
