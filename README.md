📄 Open Document Intelligence System (GenAI + RAG)

An end-to-end Retrieval-Augmented Generation (RAG) based Open Document Intelligence system that allows users to ask natural-language questions over documents and receive grounded answers using local and open-source GenAI components.

🚀 Key Features

📂 PDF Document Ingestion

✂️ Text Chunking with Overlap

🧠 Semantic Embeddings using HuggingFace

🔍 Vector Similarity Search with FAISS

🤖 Local LLM Integration using Ollama

🔗 LangChain-based RAG Orchestration

💬 Interactive CLI for user queries

🛡️ Hallucination-safe responses (context-grounded)

🧠 Why RAG?

Large Language Models can hallucinate when answering questions beyond their training data.
This system uses Retrieval-Augmented Generation (RAG) to:

Retrieve relevant document chunks

Provide them as context to the LLM

Generate answers only from the retrieved content

This ensures accuracy, transparency, and reliability.

🏗️ Architecture Overview
PDF Documents
     ↓
Document Loader
     ↓
Text Chunking
     ↓
HuggingFace Embeddings
     ↓
FAISS Vector Store
     ↓
Retriever
     ↓
Local LLM (Ollama)
     ↓
Final Answer

🛠️ Tech Stack
Component	Technology
Programming Language	Python
LLM Orchestration	LangChain
Embeddings	HuggingFace (Sentence Transformers)
Vector Database	FAISS
LLM	Ollama (local model)
Interface	Command-Line (CLI)
Version Control	Git & GitHub
📂 Project Structure
Open-Intelligence-doc/
│
├── app/
│   ├── loaders.py        # PDF loading
│   ├── chunking.py       # Text splitting logic
│   ├── embeddings.py    # Embedding generation
│   ├── retriever.py     # FAISS retriever
│   ├── rag_chain.py     # RAG pipeline
│   └── __init__.py
│
├── data/
│   └── documents/        # Sample PDFs
│
├── main.py               # Entry point (CLI)
├── pyproject.toml
├── README.md
└── .gitignore

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Manisha1808/Open-Intelligence-doc.git
cd Open-Intelligence-doc

2️⃣ Create Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


(or via pyproject.toml if using uv/poetry)

4️⃣ Install Ollama & Pull Model

Install Ollama from:
👉 https://ollama.com

Then pull a model:

ollama pull gemma:2b

▶️ Running the Application
python main.py


You will see:

Ask a question:


Example questions:

What topics do the cited papers focus on?

Summarize the document content

What research areas are discussed?

Type exit to quit.

🛡️ Hallucination Control

If the answer is not present in the document, the system responds:

"The context does not provide sufficient information to answer this question."

This ensures safe and trustworthy outputs.

📌 Design Decisions

Local LLM (Ollama)
Avoids API cost, quota limits, and privacy concerns.

FAISS for Vector Search
Fast and efficient similarity search for embeddings.

HuggingFace Embeddings
Open-source, reliable semantic representations.

LangChain
Clean abstraction for chaining retrieval and generation.

🔮 Future Enhancements

📄 Document-level summaries

🌐 FastAPI backend

📤 File upload support

📊 Answer source citations

🗂️ Multi-document indexing

🔁 Incremental ingestion

🧠 Re-ranking for better retrieval

🎯 Use Cases

Research paper analysis

Internal document Q&A

Knowledge base assistant

Educational content exploration

Private document intelligence systems

👩‍💻 Author

Manisha Sen
Computer Science Engineer | Data & GenAI Enthusiast

