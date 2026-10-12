# Task 5: ChatGPT Prompt & Output for Flipkart Product Retrieval

## 1. ChatGPT Prompt
> *"Generate 5 realistic e-commerce product titles and short descriptions for a Flipkart-style electronics and lifestyle store. Include one pair of wireless Bluetooth noise-cancelling headphones, one gaming laptop, one smartwatch, one cotton t-shirt, and one running shoe."*

---

## 2. ChatGPT Generated Products

1. **boAt Rockerz 550 Wireless Bluetooth Headphones**
   - *Description:* Over-ear wireless Bluetooth headphones with 50mm dynamic drivers, active noise cancellation, and up to 30 hours of playback.
2. **ASUS TUF Gaming F15 Laptop**
   - *Description:* High-performance 15.6-inch gaming laptop powered by Intel Core i7, 16GB DDR5 RAM, and NVIDIA GeForce RTX 4060 graphics.
3. **Noise ColorFit Pro 5 Smartwatch**
   - *Description:* Bluetooth calling smartwatch featuring a 1.85-inch AMOLED display, 24/7 heart-rate and SpO2 monitoring, and 100+ sports modes.
4. **Peter England Solid Men Polo T-Shirt**
   - *Description:* Premium 100% combed cotton regular fit polo neck casual t-shirt suitable for everyday summer wear.
5. **Nike Revolution 6 Running Shoes**
   - *Description:* Breathable mesh athletic running shoes equipped with responsive foam midsole cushioning and durable rubber traction.

---

## 3. Querying Strategy
In `task5_flipkart_faiss.py`, we generate sentence embeddings using `all-MiniLM-L6-v2` for these 5 product descriptions, index them in a normalized FAISS vector space, and perform an exact inner product similarity search for the user query: `"wireless headphones"`.
