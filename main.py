from dotenv import load_dotenv
load_dotenv()
from app.loaders import load_documents
from app.chunking import chunk_documents
from app.embeddings import create_vector_store
from app.rag_chain import build_rag_chain


docs = load_documents("data/documents")
chunks = chunk_documents(docs)

vector_store = create_vector_store(chunks)

query = "What is Retrieval Augmented Generation?"
results = vector_store.similarity_search(query, k=2)

print("\nTop matching chunks:\n")
for i, doc in enumerate(results):
    print(f"Result {i+1}:\n{doc.page_content[:300]}\n")


from app.rag_chain import build_rag_chain

rag = build_rag_chain(vector_store)

print("\n🔹 Open Document Intelligence System")
print("Type 'exit' to quit\n")

while True:
    question = input("Ask a question: ")

    if question.lower() in ["exit", "quit"]:
        print("Exiting...")
        break

    answer = rag.invoke(question)

    print("\nANSWER:\n")
    print(answer)
    print("\n" + "-" * 50 + "\n")
