# RAG with Google ADK

Retrieval-Augmented Generation (RAG) implemented as a tool inside a Google Agent Development Kit (ADK) agent — the agent retrieves relevant context from a knowledge base before answering, instead of relying solely on the model's parametric knowledge.

## Overview

This repo shows how to wire a retrieval pipeline into an ADK agent as a `FunctionTool`, so the agent decides *when* to retrieve (e.g., a question needs grounded, up-to-date, or domain-specific context) rather than retrieving unconditionally on every turn.

```
User query → Agent (LLM) → [decides to call retrieval tool] → Vector store search
                                                                      ↓
                                                          Retrieved chunks
                                                                      ↓
                                              Agent synthesizes final answer
                                              grounded in retrieved context
```

## Features

- ADK `FunctionTool` wrapping a retrieval pipeline (embed query → vector search → return top-k chunks)
- Ingestion script to chunk, embed, and index source documents
- Agent instructed to cite/ground answers in retrieved context
- *(Add: reranking, hybrid search, streaming, eval, etc. — whichever apply to your implementation)*

## Project Structure

```
rag_agent/
├── my_agent/
│   ├── __init__.py
│   └── agent.py
└── .env
|
—- setup_corpus.py

```

*(Update this tree to match your actual layout.)*

## Prerequisites

- Python 3.10+
- `pip install google-adk` (plus whatever vector store / embedding client your implementation uses)
- A Google API key (or Vertex AI credentials) for the underlying model
- Cloud Storage and sample pdf 


