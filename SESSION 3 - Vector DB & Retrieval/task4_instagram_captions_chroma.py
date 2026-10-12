import numpy as np
import chromadb

np.random.seed(101)

client = chromadb.Client()
collection = client.create_collection(name="instagram_captions")

captions = [
    "Chilling by the pool enjoying sunny weekend vibes.",
    "Sunday morning coffee and cozy blanket.",
    "Saturday night out with best friends.",
    "Late night office work grind and deadlines.",
    "Monday morning workout routine at gym.",
    "Road trip weekend adventures through the mountains."
]

dimension = 4
embeddings = np.random.random((len(captions), dimension)).tolist()
ids = [f"caption_{i}" for i in range(len(captions))]

collection.add(
    documents=captions,
    embeddings=embeddings,
    ids=ids
)

query_embedding = np.random.random((1, dimension)).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)

print("Query Target: 'Weekend vibes'\n")
print("Top 3 Retrieved Captions:")
for rank, (caption, dist) in enumerate(zip(results['documents'][0], results['distances'][0]), start=1):
    print(f"{rank}. {caption} (Distance: {dist:.4f})")

print("\nRetrieval Explanation: ChromaDB maps query vectors to vector space and uses distance metrics like squared L2 or cosine to retrieve the k-nearest indexed caption vectors.")
