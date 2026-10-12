import PyPDF2 as pdf_module

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

reader = pdf_module.PdfReader("sample_chat.pdf")

full_text = ""
for page in reader.pages:
    extracted = page.extract_text()
    if extracted:
        full_text += extracted + "\n"

chunk_size = 500
chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]

vectorizer = TfidfVectorizer()
chunk_embeddings = vectorizer.fit_transform(chunks)

def find_most_relevant_chunk(question, text_chunks, embeddings_matrix):
    query_vector = vectorizer.transform([question])
    scores = cosine_similarity(query_vector, embeddings_matrix)[0]
    best_idx = int(np.argmax(scores))
    return text_chunks[best_idx], float(scores[best_idx])

user_question = "Who messaged the most?"
matched_chunk, similarity = find_most_relevant_chunk(user_question, chunks, chunk_embeddings)

print(f"User Query: '{user_question}'\n")
print(f"Top Cosine Similarity Score: {similarity:.4f}\n")
print("Most Relevant Retrieved Chunk:")
print("=" * 60)
print(matched_chunk.strip())
print("=" * 60)
