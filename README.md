# 📄 RAG Document Search — AI-Powered PDF Question Answering

**An intelligent Retrieval-Augmented Generation (RAG) application that allows users to upload a PDF and ask natural-language questions — with answers generated strictly from the document itself.**

Built using **LangChain**, **LangGraph**, and modern LLM tooling, this project demonstrates how AI can transform static documents into interactive knowledge systems.

---

## 📋 Overview

This project implements a Retrieval-Augmented Generation pipeline designed for accuracy and traceability. Instead of relying on general knowledge, it answers questions by referencing specific data within your uploaded files.

**The Pipeline:**
1.  📝 **Ingests a PDF**
2.  ✂ **Breaks it into meaningful chunks**
3.  🧠 **Converts text into vector embeddings**
4.  🔍 **Retrieves relevant sections**
5.  🤖 **Uses an LLM to answer questions**
6.  ✅ **Ensures answers ONLY come from the document**

It utilizes a **graph-based architecture (LangGraph)**, making the pipeline modular, traceable, and production-ready.

> **Think of it as ChatGPT — but limited to your own document.**

---

## ✨ Features

* **Document-aware Question Answering:** Contextual answers derived solely from source material.
* **Zero Hallucinations:** Strict adherence to the provided document context.
* **Graph-based RAG Pipeline:** Structured flow using LangGraph for better control.
* **Modular Code Architecture:** Separation of concerns (State, Nodes, Vector Store).
* **Efficient Vector Search:** fast retrieval of semantic chunks.
* **Supports Multiple Document Types:** Extensible design.
* **Easy to Extend & Customize:** Built for developers.

---

## 🧠 Tech Stack

* **Language:** Python
* **Orchestration:** LangChain, LangGraph
* **Embeddings:** [OpenAI / HuggingFace] Embeddings
* **Vector Store:** FAISS / ChromaDB
* **LLM Provider:** [OpenAI GPT / Llama / etc.]
* **Frontend:** Streamlit

---

## 📂 Project Structure

```bash
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
│
├── main.py
├── streamlit_app.py
└── requirements.txt