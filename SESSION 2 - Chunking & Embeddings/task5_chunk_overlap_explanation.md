# Task 5: Importance of Chunk Overlap in Document Retrieval

## What is Chunk Overlap?
Chunk overlap refers to the intentional duplication of a defined number of tokens or words across consecutive chunks when splitting a long document. For instance, in a 100-word chunking strategy with a 20-word overlap, words 81–100 of Chunk 1 are repeated as words 1–20 of Chunk 2.

---

## Why Chunk Overlap is Important

1. **Preserving Semantic Context Across Boundaries:**
   - Sentences and concepts rarely end cleanly at arbitrary token or word limits. Without overlap, an important sentence, conditional statement, or entity name can be sliced in half across two disjoint chunks, destroying the semantic meaning in both vector representations.
2. **Eliminating Information Loss:**
   - Overlap guarantees that every multi-sentence relationship or transitional thought appears intact in at least one chunk embedding, ensuring high-quality vector search recall.

---

## Example Scenario: Zomato Restaurant Review Search Failure

### The Original Review:
> *"The wood-fired peri peri pizza was hands down the best dish I have ever eaten. However, immediately after eating it, the cold raw paneer sandwich gave three of my family members severe food poisoning."*

### Scenario with Zero Overlap (Chunk Size = 15 words, Overlap = 0):
- **Chunk A:** *"The wood-fired peri peri pizza was hands down the best dish I have ever eaten. However,"*
- **Chunk B:** *"immediately after eating it, the cold raw paneer sandwich gave three of my family members severe food poisoning."*

### The Problem:
1. If a customer searches on Zomato: *"Was the peri peri pizza safe to eat or did it cause food poisoning?"*
2. **Chunk A** matches on *"peri peri pizza"*, but completely misses the food poisoning consequence because the conjunction and aftermath were severed into Chunk B.
3. **Chunk B** mentions *"food poisoning"*, but the subject *"it"* loses its antecedent (*"peri peri pizza"*), causing semantic ambiguity in vector space.
4. As a result, the RAG chatbot might retrieve Chunk A and falsely answer: *"Customers loved the peri peri pizza and rated it the best dish they have ever eaten"*, failing to warn the user about severe food poisoning!

### The Solution with Overlap (Overlap = 10 words):
- **Chunk A:** *"The wood-fired peri peri pizza was hands down the best dish I have ever eaten. However,"*
- **Chunk B:** *"best dish I have ever eaten. However, immediately after eating it, the cold raw paneer sandwich gave three of my family members severe food poisoning."*
- Both the dish identity and the critical consequence remain bound together within the same semantic window.
