from sklearn.feature_extraction.text import TfidfVectorizer

reviews = [
    "The pizza was amazing",
    "Service was slow",
    "Loved the ambience"
]

vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(reviews).toarray()

for review, emb in zip(reviews, embeddings):
    print(f"Review: '{review}'")
    print(f"Vector Dimension: {len(emb)}")
    print(f"Vocabulary Features: {vectorizer.get_feature_names_out().tolist()}")
    print(f"Embedding Vector: {emb}")
    print("=" * 60)
