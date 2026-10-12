# Task 1: Introduction to Retrieval-Augmented Generation (RAG)

## What is RAG?
Retrieval-Augmented Generation (RAG) is an AI architecture that enhances the response quality of a Large Language Model (LLM) by referencing an external knowledge base before generating an answer. 

Instead of relying solely on the static knowledge stored in model weights during training, a RAG system first **retrieves** relevant facts, documents, or data matching the user's inquiry from a dedicated database (such as a vector database). It then **augments** the original user prompt with this retrieved context and passes both to the LLM to **generate** an accurate, factually grounded, and up-to-date response.

## Real-World App Improvement: Zomato Food Recommendation & Support

### Current Limitation:
In apps like Zomato, a standard LLM cannot know a restaurant's live daily menu changes, current discounts, specific dish availability, or recent customer reviews (e.g., "Is the biryani fresh today at Behrouz Biryani near Vastrapur?").

### How RAG Improves It:
With RAG integrated into Zomato's conversational assistant:
1. When a user asks: *"Suggest a top-rated spicy paneer dish under ₹300 available near me right now"*, the retrieval engine queries Zomato's live restaurant database, current pricing, inventory status, and user ratings within a 5 km radius.
2. The retrieved live records are inserted directly into the prompt context for the LLM.
3. The LLM generates a personalized, highly accurate recommendation with live prices and outlet names without hallucinating dishes that are out of stock or restaurants that are closed.
