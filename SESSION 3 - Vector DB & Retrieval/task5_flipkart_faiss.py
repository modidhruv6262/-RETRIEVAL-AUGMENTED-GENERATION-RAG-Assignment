import numpy as np
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

products = [
    {
        "title": "boAt Rockerz 550 Wireless Bluetooth Headphones",
        "desc": "Over-ear wireless Bluetooth headphones with 50mm dynamic drivers, active noise cancellation, and up to 30 hours playback."
    },
    {
        "title": "ASUS TUF Gaming F15 Laptop",
        "desc": "High-performance 15.6-inch gaming laptop powered by Intel Core i7, 16GB DDR5 RAM, and NVIDIA GeForce RTX 4060 graphics."
    },
    {
        "title": "Noise ColorFit Pro 5 Smartwatch",
        "desc": "Bluetooth calling smartwatch featuring a 1.85-inch AMOLED display, 24/7 heart-rate and SpO2 monitoring, and 100+ sports modes."
    },
    {
        "title": "Peter England Solid Men Polo T-Shirt",
        "desc": "Premium 100% combed cotton regular fit polo neck casual t-shirt suitable for everyday summer wear."
    },
    {
        "title": "Nike Revolution 6 Running Shoes",
        "desc": "Breathable mesh athletic running shoes equipped with responsive foam midsole cushioning and durable rubber traction."
    }
]

descriptions = [p["desc"] for p in products]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(descriptions).toarray().astype("float32")
faiss.normalize_L2(tfidf_matrix)

dimension = tfidf_matrix.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(tfidf_matrix)

query = "wireless headphones"
query_vector = vectorizer.transform([query]).toarray().astype("float32")
faiss.normalize_L2(query_vector)

scores, indices = index.search(query_vector, 1)

best_idx = indices[0][0]
best_score = scores[0][0]
best_product = products[best_idx]

print(f"Flipkart Search Query: '{query}'\n")
print(f"Top Matched Product: {best_product['title']}")
print(f"Similarity Score: {best_score:.4f}")
print(f"Description: {best_product['desc']}")
