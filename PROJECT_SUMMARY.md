# RAG Course - Complete Project Summary
## For AI: Read this file to understand full context and continue helping this student!

---

## WHO IS THE STUDENT?
- Name: Mahesh (based on code examples he used)
- Learning Style: Needs simple explanations, step by step, friendly tone (calls me "bro")
- Level: Beginner Python + AI
- Currently doing: DeepLearning.AI RAG Course on Coursera (Module 1 completed)
- OS Change: Moving from Windows 11 Pro to Fedora Workstation
- Has: DeepSeek API key (working and tested)
- Python version: 3.11.9

---

## WHAT WE COMPLETED

### Lab 1 — Python Refresher ✅ DONE
Key concepts learned:
- Lists: append() adds at END, insert(index, value) — index FIRST!
- append() returns NONE not the list!
- List comprehension: [x**2 for x in range(5)]
- range(1, 21) for 1 to 20 — NOT range(20)!
- Dictionaries: key:value pairs
- .items() gives keys AND values, without .items() gives only keys
- print(value) NOT print({value}) — {} creates a set!
- f-strings: f"hello {name}" — double quotes outside, single inside for dict keys
- .join() must be OUTSIDE the loop!

### Lab 2 — LLM Calls ✅ DONE
Key concepts learned:
- Tokens: 1 token ≈ 0.75 words, 100 tokens ≈ 75 words
- max_tokens controls reply length — too low = answer cut off
- 3 roles: 'user' (asking), 'assistant' (AI reply), 'system' (background instructions)
- generate_with_single_input(prompt="...") → single question
- generate_with_multiple_input(messages=[...]) → full conversation
- output is a dictionary: output['role'] and output['content']
- Always run import cell first in Jupyter!
- Augmented Prompt = YOUR DATA + question sent to LLM together

### Assignment — Introduction to RAG Systems ✅ DONE (submitted on Coursera)
Student wrote 2 functions himself:

Function 1 - get_relevant_data:
```python
def get_relevant_data(query, top_k=5):
    relevant_indices = retrieve(query, top_k)
    relevant_data = query_news(relevant_indices)
    return relevant_data
```

Function 2 - format_relevant_data:
```python
def format_relevant_data(relevant_data):
    formatted_documents = []
    for document in relevant_data:
        formatted_document = f"""
Title: {document['title']}
Description: {document['description']}
Published at: {document['published_at']}
URL: {document['url']}
        """
        formatted_documents.append(formatted_document)
    return "\n".join(formatted_documents)
```

---

## PROJECT FILES IN THIS FOLDER

| File | What it is |
|------|-----------|
| C1M1_Ungraded_Lab_1.ipynb | Python refresher lab (done) |
| C1M1_Ungraded_Lab_2.ipynb | LLM calls lab (done) |
| C1M1_Assignment.ipynb | RAG assignment (done, submitted) |
| Lab1_Questions.md | Question paper + answers for Lab 1 |
| Lab2_Questions.md | Question paper + answers for Lab 2 |
| Final_Recap_Exam.md | 25 question recap exam (not yet answered) |
| ai_news_data.py | 20 AI/Tech news items from 2026 (custom data) |
| rag_system.py | RAG system using DeepSeek API (IN PROGRESS!) |
| test.py | DeepSeek API test file |
| lists.py | Python practice |
| loops.py | Python practice |
| dictionaries.py | Python practice |
| f-strings.py | Python practice |
| exam.py | Student's coding exam answers |

---

## CURRENT STATUS — RAG SYSTEM 100% COMPLETE ✅

### We built a LOCAL RAG system using DeepSeek API!
File: rag_system.py — FULL PIPELINE WORKING END-TO-END

### All steps done in rag_system.py:
- Step 1: DeepSeek API connection — DONE and TESTED ✅
- Step 2: retrieve(query, top=5) — keyword search, returns top matching indices ✅
- Step 3: query_news(top_indices) — fetches full articles by index ✅
- Step 4: news_relevant_data(query, top=5) — combines retrieve + query_news (student wrote himself, matches assignment's get_relevant_data) ✅
- Step 5: news_format(relevant_documents) — formats articles into readable text (student wrote himself, matches assignment's format_relevant_data) ✅
- Step 6: genrate_final_prompt(query, formated_data) — builds augmented prompt ✅
- Step 7: llm_call(prompt) — sends prompt to DeepSeek, returns answer ✅
- Step 8: Final test — ran query "tell me about claude 4 and give me only url", DeepSeek correctly answered using the custom fake URL from ai_news_data.py, proving RAG (not just model's own knowledge) was used ✅

### Bugs student found and fixed himself (with hints, not full answers):
- news_format(): `.append()` was outside the for loop (only grabbed the last document) — fixed by indenting inside loop
- news_format(): `.join()` was joining the wrong variable (a single string instead of the list) — fixed to join the list
- llm_call(): forgot the `return` statement entirely — fixed by adding `return output.choices[0].message.content`

---

## NEXT STEP FOR NEW AI TO CONTINUE

The core RAG pipeline is DONE and WORKING. Possible next directions (ask student what he wants):
- Try more test queries (see TEST QUERIES section below) to explore edge cases (e.g., queries with no good matches)
- Clean up leftover debug prints (e.g., line 33 `print(retrieve(...))`)
- Move a hardcoded value out (API key is still hardcoded in source — consider env var / .env file at some point, low priority for a learning project)
- Move on to the next module of the DeepLearning.AI RAG Course on Coursera
- Optionally refactor: add error handling, docstrings, or a CLI loop for repeated questions — only if student wants to go further, not required

---

## RAG PIPELINE (final goal)

```
User Question
      ↓
retrieve(query, top_k)     → finds relevant index numbers
      ↓
query_news(indices)        → gets actual news articles
      ↓
format_relevant_data(news) → converts to readable text
      ↓
generate_final_prompt()    → combines data + question
      ↓
llm_call() with DeepSeek   → AI answers using YOUR data!
```

---

## TEST QUERIES TO USE AFTER BUILDING

- "Tell me about Claude 4"
- "Which is the best open source model in 2026?"
- "What is happening with AI and electricity?"
- "Tell me about RAG systems in 2026"
- "What did DeepSeek release?"

---

## HOW TO TALK TO THIS STUDENT

- Call him "bro" — he likes casual friendly tone
- Explain in very simple words
- Use analogies (he understood "library" analogy for retrieve/query_news)
- Don't give full code answers directly — give hints and let him figure out
- When he makes mistakes, say "almost bro!" and guide him
- He writes notes in a physical book — encourage this!
- He learns by doing — make him write code himself

---

## DEEPSEEK API DETAILS
- API key: student has it (don't store here for security)
- base_url: https://api.deepseek.com
- model: deepseek-chat
- Usage: OpenAI compatible library

```python
from openai import OpenAI
client = OpenAI(
    api_key="student's key here",
    base_url="https://api.deepseek.com"
)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "question here"}]
)
print(response.choices[0].message.content)
```

---

## IMPORTANT MISTAKES STUDENT MADE (so new AI can watch for these)

1. Forgetting to run import cell in Jupyter → NameError
2. Using range(20) instead of range(1, 21)
3. print({value}) instead of print(value)
4. .join() inside loop instead of outside
5. Using """ instead of f""" for f-strings
6. Using {raw_data} instead of {formatted_data} in prompts
7. Wrong .insert() syntax: insert('value', index) instead of insert(index, 'value')
8. Thinking .append() returns the list — it returns None!
9. Using wrong function name (generate_with_single_answer instead of generate_with_single_input)
10. Writing retrieve(query: str, top_k: int) — type annotation in function CALL

---

Good luck continuing with this student! He is hardworking and passionate about learning!
