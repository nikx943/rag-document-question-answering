# RAG-Based Document Question Answering System

A Retrieval-Augmented Generation (RAG) system for document question answering.

## Features

- PDF document upload
- PDF text extraction
- Text cleaning and chunking
- Semantic retrieval using sentence embeddings
- ChromaDB vector search
- BM25 keyword retrieval
- Reciprocal Rank Fusion (RRF)
- Cross-encoder reranking
- Ollama-based local LLM generation
- Source-grounded answers

## Architecture

PDF
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
ChromaDB + BM25
↓
Reciprocal Rank Fusion
↓
Cross-Encoder Reranking
↓
Top Relevant Chunks
↓
Ollama LLM
↓
Answer + Sources

## Technologies

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- BM25
- Ollama
- Llama 3.2
- PyPDF

## Version

Version 1.0

This version is a working prototype developed for document-based question answering.