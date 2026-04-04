# 📡 TeleRAG Scholar

### Retrieval-Augmented Generation for Telecom Research Papers

---

## 🚀 Project Overview

**TeleRAG Scholar** is a Retrieval-Augmented Generation (RAG) system designed to answer engineering questions about **telecom anomaly detection, KPI monitoring, and root cause analysis** using real research papers from arXiv.

The system retrieves relevant content from a curated corpus of telecom papers and generates **grounded, explainable answers** using a Large Language Model.

---

## 🎯 Objectives

* Build a **complete RAG pipeline**
* Work with **real-world telecom research papers**
* Understand how **retrieval quality affects LLM performance**
* Experiment with **chunking strategies**
* Deliver a **chat-based interface for querying knowledge**

---

## 🧠 System Architecture

```
User Query
   ↓
Embedding (bge-m3)
   ↓
ChromaDB (Vector Store)
   ↓
Top-K Retrieval
   ↓
Context Injection
   ↓
Mistral LLM (Ollama)
   ↓
Final Answer + Sources
```

---

## 🗂️ Project Structure

```
TeleRAG/
│
├── data/                     # PDF papers (20+ from arXiv)
├── chroma_db/               # Persistent vector database
│
├── src/
│   ├── ingestion/
│   │   ├── loader.py
│   │   ├── chunking.py
│   │   ├── populate_database.py
│
│   ├── embeddings/
│   │   ├── get_embedding_function.py
│
│   ├── retrieval/
│   │   ├── query_data.py
│   │   ├── prompt.py
│
├── app.py                   # Gradio UI
├── papers_catalog.csv       # Metadata
├── requirements.txt
└── README.md
```

---

## 📚 Dataset

* Source: **arXiv.org**
* Total Papers: **20+**
* Topics:

  * Anomaly Detection in Telecom
  * Isolation Forest / One-Class SVM
  * 5G KPI Monitoring
  * Root Cause Analysis
  * LLMs in Telecom

Each paper is stored as a PDF and tracked in:

```
papers_catalog.csv
```

Example:

```
Title | Topic | Path
-----------------------------------------
LogAnMeta | ['anomaly_detection'] | data/anomaly_detection_1.pdf
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd TeleRAG
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Install Ollama models

```
ollama pull bge-m3
ollama pull mistral
```

---

## 🔄 Pipeline Implementation

---

### 🔹 1. Document Loading

* Uses `PyPDFDirectoryLoader`
* Loads all PDFs from `/data/`

---

### 🔹 2. Chunking

* `RecursiveCharacterTextSplitter`
* Default:

  * `chunk_size = 1200`
  * `chunk_overlap = 200`

Each chunk is assigned a unique ID:

```
source:page:index
```

---

### 🔹 3. Embeddings

* Model: **bge-m3 (via Ollama)**
* Custom embedding class:

  * `embed_documents()` → for chunks
  * `embed_query()` → for user questions

---

### 🔹 4. Vector Store (ChromaDB)

* Stores:

  * embeddings
  * metadata
  * chunk IDs
* Persistent storage in `/chroma_db`

---

### 🔹 5. Query Pipeline

1. Embed user query
2. Retrieve **Top-5 similar chunks**
3. Build context
4. Send to **Mistral LLM**
5. Generate answer

---

### 🔹 6. Prompt Strategy

```
Answer ONLY from the provided context.
If not found, say "I don't know".
```

---

## 💬 Gradio Interface

Run:

```
python app.py
```

Features:

* Ask telecom-related questions
* View generated answer
* View top-3 retrieved sources (with scores)

---

## 🧪 Chunk Size Experiment

We evaluated three chunk sizes:

| Chunk Size | Overlap | Observation                  |
| ---------- | ------- | ---------------------------- |
| 400        | 80      | Too small, loses context     |
| 1200       | 200     | Balanced (best performance)  |
| 2000       | 300     | Too large, reduces precision |

### ✅ Conclusion:

Chunk size **1200** provides the best balance between:

* Context completeness
* Retrieval precision

---

<!-- ## 📊 Retrieval Evaluation (Summary)

We evaluated the system using:

* **Hit Rate**
* **Precision (relevant chunks in Top-K)**
* **Ranking Quality**

| Query | Hit | Precision | Notes             |
| ----- | --- | --------- | ----------------- |
| Q1    | Yes | 3/5       | Good              |
| Q2    | Yes | 4/5       | Very good         |
| Q3    | Yes | 2/5       | Needs improvement |
| Q4    | Yes | 3/5       | Acceptable        |
| Q5    | Yes | 3/5       | Good              | -->

<!-- --- -->

## ✅ Example Questions

The system successfully answers:

* What statistical methods are used in 5G anomaly detection?
* How does Isolation Forest work?
* What causes RRC connection failures?
* What metrics evaluate anomaly detection?
* How can LLMs assist in telecom RCA?

---

## 🔥 Key Learnings

* Retrieval quality is more important than LLM size
* Chunk size significantly affects performance
* Metadata and chunking improve interpretability
* RAG systems reduce hallucination by grounding answers

---

## 🚧 Future Improvements

* Query routing by topic (multi-folder retrieval)
* Hybrid search (BM25 + embeddings)
* Reranking models
* Deployment with Docker


---

## 📌 Notes

* All papers are open-access from arXiv
* No external API required (fully local with Ollama)

---

## ⭐ Final Remark

This project demonstrates a **complete end-to-end RAG system**, combining:

* Information Retrieval
* Embedding Models
* Vector Databases
* Large Language Models

into a real-world telecom knowledge assistant.

---
