try:
    import PyPDF2 as pdf_module
except ImportError:
    import pypdf as pdf_module

reader = pdf_module.PdfReader("sample_resume.pdf")

extracted_text = ""
for page_num, page in enumerate(reader.pages, start=1):
    text = page.extract_text()
    if text:
        extracted_text += text + "\n"

print(f"Total Pages in PDF: {len(reader.pages)}")
print("=" * 60)
print("EXTRACTED RESUME TEXT:")
print("=" * 60)
print(extracted_text.strip())
