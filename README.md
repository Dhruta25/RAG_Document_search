📄 RAG Document Search — AI-Powered PDF Question Answering

An intelligent Retrieval-Augmented Generation (RAG) application that allows users to upload a PDF and ask natural-language questions — with answers generated strictly from the document itself. Built using LangChain, LangGraph, and modern LLM tooling, this project demonstrates how AI can transform static documents into interactive knowledge systems.

📋 Overview

This project implements a Retrieval-Augmented Generation pipeline that:

📝 Ingests a PDF
✂ Breaks it into meaningful chunks
🧠 Converts text into vector embeddings
🔍 Retrieves relevant sections
🤖 Uses an LLM to answer questions
✅ Ensures answers ONLY come from the document

It follows a graph-based architecture using LangGraph — making the pipeline modular, traceable, and production-ready.

Think of it as ChatGPT — but limited to your own document.

✨ Features
	•	Document-aware Question Answering
	•	Zero Hallucinations
	•	Graph-based RAG Pipeline
	•	Modular Code Architecture
	•	Efficient Vector Search
	•	Supports Multiple Document Types
	•	Easy to Extend & Customize

🧠 Tech Stack
	•	Python
	•	LangChain
	•	LangGraph
	•	Embeddings Model
	•	Vector Store (FAISS / Similar)
	•	LLM Provider
	•	Document Loaders


RAG_Document_Search
│
├── data/                    
│   ├── Dhruta_resume.pdf
│   └── url.txt
│
├── src/                      
│   ├── state/
│   │   ├── __init__.py
│   │   └── rag_state.py
│   │
│   ├── vectorstore/
│   │   ├── __init__.py
│   │   └── vectorstore.py
│   │
│   ├── graph_builder/
│   │   ├── __init__.py
│   │   └── graph_builder.py
│   │
│   ├── node/
│   │   ├── __init__.py
│   │   ├── nodes.py
│   │   └── reactnode.py
│   │
│   └── document_ingestion/
│       ├── __init__.py
│       └── document_process.py
|___main.py
|___streamlit_app.py
|___requirements.txt


🔍 How It Works

1️⃣ Upload a PDF
The document is read and converted to clean text

2️⃣ Chunking & Embeddings
The text is split and embedded

3️⃣ Vector Indexing
Chunks are stored for semantic search

4️⃣ User Asks a Question
Relevant chunks are retrieved

5️⃣ RAG-Based Answering
The LLM responds using only your document

🎯 No external data
🎯 No hallucinations
🎯 Reliable context-aware answers


🏗️ Architecture (LangGraph Workflow)

The system runs as a graph pipeline consisting of:

🔹 Document Loader Node
🔹 Chunk Processor Node
🔹 Embedding Node
🔹 Vector Retrieval Node
🔹 LLM Response Node

This makes the flow:

✨ Traceable
✨ Scalable
✨ Production-ready
