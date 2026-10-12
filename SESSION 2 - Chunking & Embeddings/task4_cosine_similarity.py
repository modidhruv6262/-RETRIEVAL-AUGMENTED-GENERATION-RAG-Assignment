from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentence_1 = "The burger was delicious"
sentence_2 = "I enjoyed the burger a lot"

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([sentence_1, sentence_2])

similarity_score = float(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0])

print(f"Sentence 1: '{sentence_1}'")
print(f"Sentence 2: '{sentence_2}'")
print(f"Cosine Similarity Score: {similarity_score:.4f}")

if similarity_score > 0.1:
    print("Interpretation: Semantically similar. Both sentences share key vocabulary relating to the burger satisfaction.")
else:
    print("Interpretation: Low vocabulary overlap.")
