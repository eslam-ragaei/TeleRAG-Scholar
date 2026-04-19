# 📡 TeleRAG Scholar (Microservices RAG System)

## 🚀 Overview

TeleRAG Scholar is a **production-style microservices Retrieval-Augmented Generation (RAG) system** designed for telecom research papers.

It enables intelligent question answering over a corpus of telecom papers using:
- Dense semantic retrieval (BGE-M3)
- Cross-encoder reranking
- Large Language Model reasoning (Mistral)
- Fully modular microservices architecture

The system is designed to evolve from an **MVP RAG system (Level 1)** into an **industry-grade AI knowledge platform (Level 2 & 3 roadmap)**.

---

## 🧠 System Architecture

### 🔷 RAG system flow

<img src="RAG system.png">

---

### 🔷 Microservices Design

#### System Architecture Diagram

<img src="Microservices Design.png">

---

## ⚙️ Core Services

### 🟢 API Gateway
- Entry point of the system
- Routes requests between services
- Aggregates final response
- Returns answer + sources

---

### 🟢 Ingestion Service
Responsible for building the knowledge base:

- Loads PDF documents
- Extracts raw text
- Splits into semantic chunks
- Generates embeddings using **BGE-M3**
- Stores chunks + embeddings into **ChromaDB**

---

### 🟢 Retrieval Service
Core search engine of the system:

- Converts query into embeddings (BGE-M3)
- Performs vector similarity search in ChromaDB
- Retrieves top-K candidate chunks
- Applies **Cross-Encoder reranking**
- Returns most relevant context

---

### 🟢 LLM Service
Reasoning and answer generation:

- Uses **Mistral LLM (Ollama / HF)**
- Receives retrieved context
- Generates grounded response
- Ensures answers are based only on provided context

---

### 🟢 Vector Database (ChromaDB)
- Stores embeddings and metadata
- Persistent storage via Kubernetes PVC
- Enables fast semantic search

---

## 📁 Project Structure

### Directory Structure

- **services/**
  - **api-gateway/**
    - `main.py`
  - **ingestion-service/**
    - `app.py`
    - `loader.py`
    - `chunker.py`
    - `embedder.py`
  - **retrieval-service/**
    - `app.py`
    - `retriever.py`
    - `reranker.py`
  - **llm-service/**
    - `app.py`
    - `client.py`

- **shared/**
  - `embeddings.py`
  - `config.py`

- **data/** _# local development only_
- **chroma_db/** _# persistent volume (K8s)_

- **docker/**
  - `Dockerfile.api`
  - `Dockerfile.ingestion`
  - `Dockerfile.retrieval`
  - `Dockerfile.llm`

- **k8s/**
  - `api-deployment.yaml`
  - `ingestion-deployment.yaml`
  - `retrieval-deployment.yaml`
  - `llm-deployment.yaml`
  - `chroma-pvc.yaml`
  - `services.yaml`

- Root files:
  - [`docker-compose.yml`](docker-compose.yml)
  - [`requirements.txt`](requirements.txt)
  - [`README.md`](README.md)

---

## 🧠 Data Flow

### 🔷 Query Flow
#### Workflow Diagram

- **User Question**
- **API Gateway**
- **Retrieval Service**
- **BGE-M3 Embedding**
- **ChromaDB Vector Search**
- **Cross-Encoder Reranker**
- **Top-K Context**
- **LLM Service (Mistral)**
- **Final Answer + Sources**

---

### 🔷 Ingestion Flow

#### PDF Documents Workflow

1. **PDF Documents**
2. **Ingestion Service**
3. **Text Extraction**
4. **Chunking Strategy**
5. **BGE-M3 Embeddings**
6. **ChromaDB Storage**

---

## 📦 Model Strategy (Kubernetes Design)

### 🟢 BGE-M3 (Embedding Model)
- Loaded from HuggingFace (`BAAI/bge-m3`)
- Cached inside container runtime
- Stateless per pod

---

### 🟢 Mistral (LLM Model)
- Runs via Ollama service
- Stored in Kubernetes Persistent Volume (PVC)
- Reused across pod restarts

---

## ⚙️ Installation (Local Development)

```bash
git clone <repo>
cd telerag-scholar
pip install -r requirements.txt
```

### Run with Docker

```bash
docker compose up --build
```

### Deploy with Kubernetes

```bash
kubectl apply -f k8s/
```

---

## 🧪 Current System (MVP - Level 1)

This system currently supports:

- Dense retrieval using BGE-M3
- Cross-encoder reranking
- Context-based LLM answering (Mistral)
- ChromaDB vector storage
- Basic evaluation of retrieval quality

---

## 📊 Evaluation Strategy

- Hit Rate (retrieval success)
- Precision@K
- Chunk relevance score
- Answer grounding correctness

---

## 🚧 Roadmap

### 🟢 Level 1 (Completed MVP)
- Dense retrieval
- Reranking
- LLM-based generation
- Basic RAG pipeline

### 🟡 Level 2 (Next Upgrade)
- Query rewriting module
- Metadata-based filtering
- Automatic evaluation pipeline
- Logging and monitoring system
- Citation grounding improvements

### 🔴 Level 3 (Advanced System)
- Hybrid retrieval (BM25 + dense)
- Multi-stage ranking pipeline
- Feedback learning loop
- A/B testing system
- Large-scale production RAG architecture

---

## 🧠 Key Insight
This project is designed as a distributed AI knowledge system, not a simple script.
It separates:
- Retrieval (search intelligence)
- Ranking (relevance intelligence)
- Generation (language intelligence)

---

## ⭐ Final Note
TeleRAG Scholar demonstrates a complete end-to-end RAG system architecture, combining:
- Information Retrieval
- Embedding Models
- Vector Databases
- Re-ranking Models
- Large Language Models
- Microservices Design
- Kubernetes Deployment