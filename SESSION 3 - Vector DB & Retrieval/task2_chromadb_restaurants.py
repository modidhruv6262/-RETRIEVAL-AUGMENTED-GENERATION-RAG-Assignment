import numpy as np
import chromadb

np.random.seed(42)

client = chromadb.Client()
collection = client.create_collection(name="restaurants")

restaurant_names = [
    "Barbeque Nation",
    "Domino's Pizza",
    "Haldiram's",
    "Subway",
    "KFC"
]

embeddings = np.random.random((5, 3)).tolist()
ids = [f"rest_{i}" for i in range(5)]

collection.add(
    documents=restaurant_names,
    embeddings=embeddings,
    ids=ids
)

query_vector = np.random.random((1, 3)).tolist()

results = collection.query(
    query_embeddings=query_vector,
    n_results=1
)

most_similar_restaurant = results['documents'][0][0]
distance = results['distances'][0][0]

print(f"Total restaurants in collection: {collection.count()}")
print(f"Query Vector: {query_vector[0]}")
print(f"Most similar restaurant: {most_similar_restaurant}")
print(f"Distance: {distance:.4f}")
