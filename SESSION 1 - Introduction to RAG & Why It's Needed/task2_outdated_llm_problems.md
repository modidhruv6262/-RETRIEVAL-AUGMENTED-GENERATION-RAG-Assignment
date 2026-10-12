# Task 2: Outdated LLM Knowledge & Limitations

## Scenario
A travel assistant chatbot powered by an LLM whose training cutoff is the year **2022**.

## 3 Questions the Bot Would Struggle to Answer

### 1. IRCTC Vande Bharat Express Schedule
- **Question:** *"What is the departure timing and schedule of the Ahmedabad to Mumbai Central Vande Bharat Express (Train No. 22962) on Wednesdays?"*
- **Why the bot struggles:** Several new Vande Bharat Express routes, updated station halts, and modified weekly operational days were introduced by Indian Railways in late 2023 and 2024. A 2022-trained model does not possess schedule data for trains inaugurated after its cutoff date.

### 2. IPL 2024 Captaincy & Squad Changes
- **Question:** *"Who was the captain of Mumbai Indians during IPL 2024, and did they qualify for the playoffs?"*
- **Why the bot struggles:** The major leadership change where Hardik Pandya replaced Rohit Sharma as Mumbai Indians captain occurred ahead of the 2024 season. A 2022 model would confidently declare Rohit Sharma as the active captain and have no record of the 2024 points table or playoff qualification.

### 3. IRCTC Tatkal & Dynamic Pricing Rules
- **Question:** *"What are the current cancellation refund rules and dynamic surge pricing caps for IRCTC Tatkal tickets in 2024?"*
- **Why the bot struggles:** Indian Railways frequently revises booking cancellation fees, tatkal refund percentages, and automated passenger quota algorithms. The 2022 model would quote obsolete policies that could mislead a traveler financial planning their journey.

---

## Why Outdated LLM Knowledge is a Problem
1. **Hallucination Risk:** Rather than admitting ignorance, LLMs frequently generate plausible-sounding but completely incorrect schedules, train numbers, or match results.
2. **Real-World Consequences:** Relying on outdated train timings can cause travelers to miss their trains or book incorrect routes, causing direct financial loss and severe inconvenience.
3. **Inability to Self-Update:** Standard LLM weights are frozen upon completion of pre-training. Without a retrieval mechanism like RAG connecting the bot to live databases or APIs, the assistant remains permanently stuck in the past.
