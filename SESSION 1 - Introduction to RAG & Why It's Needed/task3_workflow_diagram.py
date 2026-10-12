def display_rag_workflow():
    steps = [
        "============================================================",
        "          RETRIEVAL-AUGMENTED GENERATION (RAG) WORKFLOW     ",
        "============================================================",
        " [Step 1: User Query] ",
        "         |",
        "         |---> 'What is the schedule of Train 22962?'",
        "         v",
        " [Step 2: Retrieve Documents] ",
        "         |",
        "         |---> Query Embedding -> Cosine Similarity Search",
        "         |---> Knowledge Base / Vector DB (ChromaDB / FAISS)",
        "         |---> Relevant Chunks Fetched: 'Train 22962 departs at 06:10 AM'",
        "         v",
        " [Step 3: Combine with LLM (Prompt Augmentation)] ",
        "         |",
        "         |---> Context: 'Retrieved official IRCTC timetable'",
        "         |---> Question: 'User query'",
        "         |---> Prompt fed to LLM (e.g., Llama 3 via Groq)",
        "         v",
        " [Step 4: Generate Answer] ",
        "         |",
        "         v",
        " 'Train 22962 departs Ahmedabad at 06:10 AM on Wednesdays.'",
        "============================================================"
    ]
    for step in steps:
        print(step)

if __name__ == "__main__":
    display_rag_workflow()
