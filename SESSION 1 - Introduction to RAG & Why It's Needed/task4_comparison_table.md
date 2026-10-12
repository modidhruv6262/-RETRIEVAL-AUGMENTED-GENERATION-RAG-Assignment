# Task 4: Comparison Table - RAG vs Fine-Tuning vs Prompt Engineering

| Dimension | Retrieval-Augmented Generation (RAG) | Fine-Tuning | Prompt Engineering |
| :--- | :--- | :--- | :--- |
| **Cost** | **Low to Moderate**<br>Cost of embedding generation and vector database hosting; standard LLM API inference costs. | **High**<br>Requires significant GPU compute resources, high memory, training datasets, and engineering hours. | **Very Low**<br>Minimal cost; only standard token usage for prompt design and iterations. |
| **Data Freshness** | **Real-Time / Dynamic**<br>Documents and database entries can be updated, inserted, or deleted instantly without retraining the model. | **Static / Frozen**<br>Knowledge is frozen at the moment training completes. Updates require triggering an entire retraining pipeline. | **Limited to Context Window**<br>Only as fresh as the short reference text manually pasted into the system prompt. |
| **Use Case Example** | **Zomato / Swiggy Customer Support**<br>Chatbot answering live order refund policies, tracking real-time delivery status, and restaurant menu queries. | **BloombergGPT / Medical Diagnostic Models**<br>Teaching an LLM custom syntax, specialized medical jargon, or unique proprietary coding styles. | **Format Customization**<br>Instructing ChatGPT to output responses strictly in JSON, or styling customer greetings like Spotify playlist descriptions. |
| **Speed of Implementation** | **Fast (Hours to Days)**<br>Connect a document chunking pipeline to ChromaDB/FAISS and integrate with LangChain. | **Slow (Weeks to Months)**<br>Requires data curation, cleaning, validation, hyperparameter tuning, and rigorous safety alignment. | **Immediate (Minutes)**<br>Can be prototyped, tested, and modified instantly in a single prompt playground. |

---

## Key Synthesis
- **Prompt Engineering** is ideal for adjusting style, tone, and formatting constraints.
- **Fine-Tuning** is optimal for adapting model behavior, dialect, syntax, or tone to specialized domains where fundamental vocabulary needs to change.
- **RAG** is the gold standard when accurate factual recall, live document updates, and verification of reference sources are strictly required.
