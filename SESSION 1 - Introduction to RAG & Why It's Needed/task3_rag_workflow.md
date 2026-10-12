# Task 3: Basic RAG Workflow Diagram

## Flowchart Representation

```mermaid
flowchart TD
    A["👤 User Query\n('What is the schedule of Train 22962?')"] --> B["🔍 Query Embedding & Semantic Search"]
    
    subgraph Knowledge Base ["External Knowledge Base"]
        D1[("📚 Vector DB / Documents\n(IRCTC Timetables, Policies, Live DB)")]
    end
    
    B <--> D1
    B --> C["📄 Retrieved Relevant Chunks\n('Train 22962 departs Ahmedabad at 06:10 AM...')"]
    
    A --> E["🧩 Prompt Augmentation"]
    C --> E
    
    E --> F["🤖 Large Language Model (LLM)\n(Context + Query)"]
    F --> G["💬 Grounded Response\n('Train 22962 departs Ahmedabad at 06:10 AM on Wednesdays.')"]
```

---

## Detailed Step-by-Step Breakdown

1. **User Query:** The user inputs an arbitrary natural language question into the interface.
2. **Retrieve Documents:** The query is converted into an embedding vector, and a similarity search is performed against a vector database storing indexed documents, reports, or records.
3. **Combine with LLM (Augmentation):** The top matching document chunks are combined with the user query into a structured prompt template.
4. **Generate Answer:** The LLM reads both the query and the exact retrieved reference facts to produce a strictly grounded, hallucination-free answer.
