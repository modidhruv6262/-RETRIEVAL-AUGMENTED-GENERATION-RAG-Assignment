def chunk_text(text, chunk_size, overlap):
    words = text.split()
    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        if i + chunk_size >= len(words):
            break
    return chunks

zomato_privacy_policy = """
Zomato is committed to protecting the privacy of its users and customers. This Privacy Policy describes how Zomato Media Private Limited and its affiliates collect use share and protect the personal information of individuals who visit our websites mobile applications and online food ordering platforms. When you use our services we may collect your personal information including your full name email address contact number delivery address geographical location and payment method information. We collect device information such as device model operating system unique device identifiers and mobile network details to improve our services and troubleshoot bugs. We process location data to provide delivery tracking suggest nearby restaurants calculate delivery fees and display estimated preparation times. We also collect transaction details including items ordered payment transactions customer support tickets and rating reviews you publish on our platform. We may share information with restaurant partners and third-party delivery personnel strictly to complete the fulfillment of your food delivery order. We also share data with payment gateway service providers fraud prevention agencies and marketing partners where you have consented. We use cookies and similar tracking technologies to store session preferences and enhance user experience across web sessions. Users have the right to request access rectification or deletion of their personal information at any time through account settings or by contacting our Data Protection Officer. We implement technical and administrative security measures designed to protect your personal data from unauthorized access disclosure alteration and destruction. By using the Zomato platform you agree to the collection and use of information in accordance with this policy.
"""

chunks = chunk_text(zomato_privacy_policy, 100, 20)

print(f"Total Words in Policy: {len(zomato_privacy_policy.split())}")
print(f"Total Chunks Generated: {len(chunks)}\n")

for i in range(min(3, len(chunks))):
    print(f"==================== CHUNK {i + 1} ====================")
    print(chunks[i])
    print()
