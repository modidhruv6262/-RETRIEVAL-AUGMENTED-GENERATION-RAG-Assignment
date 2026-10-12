import PyPDF2 as pdf_module

from sklearn.feature_extraction.text import TfidfVectorizer

reader = pdf_module.PdfReader("sample_chat.pdf")

full_text = ""
for page in reader.pages:
    extracted = page.extract_text()
    if extracted:
        full_text += extracted + "\n"

chunk_size = 500
chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]

vectorizer = TfidfVectorizer()
chunk_embeddings = vectorizer.fit_transform(chunks).toarray().tolist()

print(f"Total chunks embedded: {len(chunk_embeddings)}")
print(f"Embedding vector dimension: {len(chunk_embeddings[0])}")
print("First chunk preview:")
print(chunks[0][:120].strip() + "...\n")
print(f"Embedding vector for Chunk 1 (first 5 elements): {chunk_embeddings[0][:5]}")
