# Lab 2 - LLM Calls and Augmented Prompts: Question Paper
### Completed and Corrected!

---

## SECTION A - Theory Questions

**Q1.** What is the difference between `generate_with_single_input` and `generate_with_multiple_input`?

✅ YOUR ANSWER: single input = one question no context, multiple input = full conversation with context history — CORRECT!

---

**Q2.** What is a token? Roughly how many words is 100 tokens?

⚠️ YOUR ANSWER: Said 100 tokens = 200 words — WRONG
✅ CORRECT ANSWER:
- A token is a chunk of text (part of a word or full word)
- 1 token ≈ 0.75 words
- 100 tokens ≈ 75 words (NOT 200!)
- Example: "Artificial" = 2 tokens, "Hello" = 1 token

---

**Q3.** What happens if `max_tokens` is too low?

✅ YOUR ANSWER: Answer gets cut off in the middle — CORRECT! Great room size analogy too!

---

**Q4.** What are the 3 valid roles in an LLM message?

⚠️ YOUR ANSWER: Only said user and assistant, confused content with role — WRONG
✅ CORRECT ANSWER: There are 3 roles:
```
1. 'user'      → the person asking the question
2. 'assistant' → the AI giving the answer
3. 'system'    → background instructions given to AI before conversation
                  Example: "You are a helpful assistant who only answers about cricket"
```
content is NOT a role — it is a KEY inside the message dictionary!

---

**Q5.** What is an Augmented Prompt?

✅ YOUR ANSWER: Sending user query + data both to LLM together — CORRECT!

---

**Q6.** Why does giving house data give better answers?

✅ YOUR ANSWER: Without data AI uses training data (may be wrong), with data AI uses your specific accurate data — CORRECT!

---

**Q7.** Why pass full conversation history to `generate_with_multiple_input`?

⚠️ YOUR ANSWER: "i dont know"
✅ CORRECT ANSWER: Because AI has no memory between messages! Without history it loses context:
```
User:      "Who is Virat Kohli?"
AI:        "He is a cricketer."
User:      "How old is he?"       ← AI doesn't know WHO "he" is without history!
```
With full history → AI reads all previous messages → knows "he" = Virat Kohli → answers correctly!

---

## SECTION B - Predict the Output

**Q8.** What will this print?

⚠️ YOUR ANSWER: 3rd print said "content" — WRONG
✅ CORRECT ANSWER:
```
2              ← len(messages) = 2 items in list
user           ← messages[0]['role'] = 'user'
Hi there!      ← messages[1]['content'] = 'Hi there!' (the VALUE not the key name!)
```

---

**Q9.** What is wrong with the code run in a fresh notebook?

✅ YOUR ANSWER: NameError — generate_with_single_input not defined because import cell not run — CORRECT!

---

**Q10.** What will this print?

⚠️ YOUR ANSWER: Bob's score was 95 — WRONG (you copied Alice's score)
✅ CORRECT ANSWER:
```
Name: Alice, Score: 95
Name: Bob, Score: 80

```
(Bob's score is 80 not 95! Always read the data carefully!)

---

## SECTION C - Coding Questions

**Q11.** Call LLM asking about Machine Learning, print only content.

✅ YOUR ANSWER: CORRECT!
```python
ans = generate_with_single_input(
    prompt="What is machine learning?"
)
print(ans['content'])
```

---

**Q12.** Create 3-message cricket conversation and call generate_with_multiple_input.

✅ YOUR ANSWER: CORRECT! (comma was there between all dictionaries)
```python
data = [
    {'role': 'user', 'content': 'tell me about cricket'},
    {'role': 'assistant', 'content': 'cricket is a sports'},
    {'role': 'user', 'content': 'who win first world cup tell me in one line'}
]
output = generate_with_multiple_input(messages=data, max_tokens=100)
print(output['content'])
```

---

**Q13.** Write movie_info_layout function.

⚠️ YOUR ANSWER: Missing quotes around dict keys — ERROR
✅ CORRECT ANSWER:
```python
def movie_info_layout(movies):
    layout = ''
    for movie in movies:
        layout += (f"Movie: {movie['title']}, Year: {movie['year']}, "
                   f"Genre: {movie['genre']}, Rating: {movie['rating']}\n")
    #                        ^^^^^^^^               ^^^^^^^^^
    #                   need quotes around keys!    and \n at end!
    return layout
```
Key fixes:
- moive['genre'] not moive[genre] — keys need quotes!
- Add \n at end for new line between each movie

---

**Q14.** Write generate_movie_prompt function.

⚠️ YOUR ANSWER: Missing f before triple quotes — variables won't be replaced!
✅ CORRECT ANSWER:
```python
def generate_movie_prompt(query, movies):
    full_info = movie_info_layout(movies)
    prompt = f"""
tell me answers based on below data
{full_info}
Query: {query}
    """
    #  ↑ f""" not just """ — without f, {full_info} prints literally as text!
    return prompt
```
Key fix: `f"""` not `"""` — need the f prefix for variables to work inside!

---

**Q15.** Difference between two calls?

✅ YOUR ANSWER: Call 1 = AI uses training data (random), Call 2 = AI uses your movie data (accurate) — CORRECT!

---

## SECTION D - Bonus

**Q16.** What is wrong with the get_info function?

✅ YOUR ANSWER: Missing return layout inside function — CORRECT!
```python
def get_info(data):
    layout = ''
    for item in data:
        layout += f"Name: {item['name']}\n"
    return layout    # ← this was missing!
```

---

**Q17.** What is wrong with using generate_with_single_input for multiple messages?

✅ YOUR ANSWER: Should use generate_with_multiple_input — CORRECT!
```python
output = generate_with_multiple_input(messages=messages)  # ✅ correct
```

---

**Q18.** Why is RAG needed?

✅ YOUR ANSWER: Excellent! Milk shop example is perfect — LLM doesn't know real-time data, RAG solves this by sending your data + question together — CORRECT!

---

**Total: 18 Questions**
**Your Score: 12.5/18 → Improved from Lab 1! Keep going!**

---

## KEY THINGS TO REMEMBER (from mistakes):

| Mistake | Correct |
|---|---|
| 100 tokens = 200 words | 100 tokens ≈ 75 words |
| Only 2 roles | 3 roles: user, assistant, system |
| range(20) for 1 to 20 | range(1, 21) |
| print({value}) | print(value) |
| .join() inside loop | .join() OUTSIDE loop |
| .append() returns list | .append() returns None! |
| f""" missing f | Always f""" for variables |
| dict key without quotes | Always use dict['key'] with quotes |
