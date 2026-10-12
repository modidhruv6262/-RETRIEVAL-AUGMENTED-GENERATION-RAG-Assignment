try:
    import PyPDF2 as pdf_module
except ImportError:
    import pypdf as pdf_module

reader = pdf_module.PdfReader("sample_chat.pdf")

full_text = ""
for page in reader.pages:
    extracted = page.extract_text()
    if extracted:
        full_text += extracted + "\n"

chunk_size = 500
chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]

print(f"Total characters extracted from PDF: {len(full_text)}")
print(f"Total chunks created (500 chars each): {len(chunks)}\n")

for index, chunk in enumerate(chunks, start=1):
    print(f"==================== CHUNK {index} ({len(chunk)} characters) ====================")
    print(chunk.strip())
    print()
