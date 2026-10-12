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

wikipedia_sample = """
Artificial intelligence is the intelligence of machines or software as opposed to the intelligence of living beings primarily humans. It is a field of study in computer science that develops and studies intelligent machines. Such machines may be called AIs. AI technology is widely used throughout industry government and science. Some high-profile applications include advanced web search engines such as Google Search recommendation systems used by YouTube Amazon and Netflix understanding human speech such as Google Assistant Siri and Alexa self-driving cars such as Waymo generative and creative tools such as ChatGPT and super-human play and analysis in strategy games such as chess and Go. Alan Turing was the first person to conduct substantial research in the field that he called machine intelligence. Artificial intelligence was founded as an academic discipline in 1956. The field went through multiple cycles of optimism followed by periods of disappointment and loss of funding known as AI winters. Funding and interest vastly increased after 2012 when deep learning surpassed all previous AI techniques and after 2017 with the transformer architecture. This led to the AI boom of the early 2020s with widespread commercial deployment of machine learning systems. The various sub-fields of AI research are centered around particular goals and the use of particular tools. The traditional goals of AI research include reasoning knowledge representation planning learning natural language processing perception and support for robotics. General intelligence the ability to solve an arbitrary problem is among the field's long-term goals. To solve these problems AI researchers have adapted and integrated a wide range of problem-solving techniques including search and mathematical optimization formal logic artificial neural networks and methods based on statistics operations research and economics. AI also draws upon psychology linguistics philosophy neuroscience and other fields. Machine learning is a subfield of artificial intelligence that studies algorithms that automatically improve through experience and with data. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data known as training data in order to make predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide variety of applications such as in medicine email filtering speech recognition agriculture and computer vision where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks. A subset of machine learning is closely related to computational statistics which focuses on making predictions using computers but not all machine learning is statistical learning. The study of mathematical optimization delivers methods theory and application domains to the field of machine learning. Data mining is a related field of study focusing on exploratory data analysis through unsupervised learning. Some implementations of machine learning use data and neural networks in a way that mimics the working of a biological brain. Deep learning is part of a broader family of machine learning methods based on artificial neural networks with representation learning. The adjective deep in deep learning refers to the use of multiple layers in the network.
"""

chunks = chunk_text(wikipedia_sample, 100, 20)

print(f"Total words in sample: {len(wikipedia_sample.split())}")
print(f"Total chunks created: {len(chunks)}\n")

for index, chunk in enumerate(chunks, start=1):
    print(f"--- Chunk {index} (Words: {len(chunk.split())}) ---")
    print(chunk[:120] + "...")
    print()
