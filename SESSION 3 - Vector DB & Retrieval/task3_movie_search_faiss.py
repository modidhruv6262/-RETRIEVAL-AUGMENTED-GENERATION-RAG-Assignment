import numpy as np
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

movie_titles = [
    "Mad Max: Fury Road",
    "The Notebook",
    "John Wick",
    "Superbad",
    "The Conjuring"
]

movie_descriptions = [
    "High octane desert car chases and explosive action battles.",
    "A romantic love story spanning decades between two devoted lovers.",
    "A former hitman unleashes ruthless gunplay and martial arts action vengeance.",
    "Two high school friends go on a hilarious misadventure before graduation.",
    "Paranormal investigators encounter terrifying supernatural demonic entities."
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movie_descriptions).toarray().astype("float32")
faiss.normalize_L2(tfidf_matrix)

dimension = tfidf_matrix.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(tfidf_matrix)

user_query = "action movie"
query_vector = vectorizer.transform([user_query]).toarray().astype("float32")
faiss.normalize_L2(query_vector)

top_k = 2
distances, indices = index.search(query_vector, top_k)

print(f"Search Query: '{user_query}'\n")
print("Top 2 Most Similar Movies:")
for rank in range(top_k):
    idx = indices[0][rank]
    score = distances[0][rank]
    print(f"{rank + 1}. {movie_titles[idx]} (Similarity Score: {score:.4f})")
    print(f"   Plot: {movie_descriptions[idx]}")
