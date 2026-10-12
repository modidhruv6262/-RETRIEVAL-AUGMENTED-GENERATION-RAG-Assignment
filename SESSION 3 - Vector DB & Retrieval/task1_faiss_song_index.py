import numpy as np
import faiss

np.random.seed(42)
dimension = 4
num_songs = 5

song_embeddings = np.random.random((num_songs, dimension)).astype("float32")

index = faiss.IndexFlatL2(dimension)
index.add(song_embeddings)

print(f"Number of song vectors in FAISS index: {index.ntotal}")
print(f"Vector dimension: {index.d}")
print(f"Index training status: {index.is_trained}")
print("Generated song vectors:")
print(song_embeddings)
