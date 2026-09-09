# FINAL RECAP EXAM — RAG Course Module 1
### Covers: Python Basics + LLM Calls + RAG System
### Write answers yourself — no cheating bro!

---

## SECTION A — Python Basics (Lab 1)

**Q1.** What are the 3 topics covered in Lab 1?

**Q2.** What is the output?
```python
fruits = ['apple', 'mango', 'banana']
fruits.append('grape')
fruits.remove('mango')
print(fruits[1])
```

**Q3.** Fix the mistake:
```python
l1 = ['a', 'b', 'c']
l1.insert('d', 1)
```

**Q4.** What is the output?
```python
nums = [x**2 for x in range(6) if x % 2 != 0]
print(nums)
```

**Q5.** What is the output?
```python
l = [10, 20, 30]
result = l.append(40)
print(result)
print(l)
```

**Q6.** What is wrong here?
```python
student = {'name': 'Ravi', 'age': 21}
for key, value in student.items():
    print({value})
```

**Q7.** Write a list comprehension to get all names from this list that have more than 4 letters:
```python
names = ['Raj', 'Priya', 'Ali', 'Mahesh', 'Tom']
```

**Q8.** What is the output?
```python
person = {'city': 'Chennai', 'age': 25}
for val in person:
    print(val)
```

**Q9.** Create a dictionary called `phone` with keys: `brand`, `model`, `price`. Print each key and value using `.items()` with an f-string like:
```
brand : Samsung
model : S24
price : 80000
```

---

## SECTION B — LLM Calls (Lab 2)

**Q10.** What are the 3 valid roles in an LLM message? Explain each in one line.

**Q11.** 100 tokens = roughly how many words?

**Q12.** What is the difference between `generate_with_single_input` and `generate_with_multiple_input`? When do you use each?

**Q13.** What is wrong here?
```python
messages = [
    {'role': 'user', 'content': 'What is cricket?'}
    {'role': 'assistant', 'content': 'Cricket is a sport.'}
    {'role': 'user', 'content': 'Who invented it?'}
]
output = generate_with_single_input(messages=messages)
```
(There are 2 mistakes — find both!)

**Q14.** What will this print?
```python
messages = [
    {'role': 'user', 'content': 'Hello'},
    {'role': 'assistant', 'content': 'Hi!'},
    {'role': 'user', 'content': 'How are you?'}
]
print(len(messages))
print(messages[2]['content'])
print(messages[1]['role'])
```

**Q15.** What is an Augmented Prompt? Give one real life example of why it's needed.

**Q16.** Write a function `create_prompt(query, data_text)` that combines data and query into a prompt using f-string triple quotes. The prompt should tell the LLM to use the data to answer the query.

---

## SECTION C — RAG System (Assignment)

**Q17.** Explain the full RAG pipeline in your own words. What happens step by step from user question to final answer?

**Q18.** What does `retrieve(query, top_k)` return? What does `query_news(indices)` return?

**Q19.** What is the difference between these two?
```python
result1 = llm_call("Who won IPL 2024?", use_rag=False)
result2 = llm_call("Who won IPL 2024?", use_rag=True)
```
Which gives more accurate answer and why?

**Q20.** Write the complete `get_relevant_data` function from memory:
```python
def get_relevant_data(query, top_k=5):
    # write 2 lines here
```

**Q21.** Write the complete `format_relevant_data` function from memory. It must include title, description, published_at and url.

**Q22.** What is wrong here?
```python
def format_relevant_data(relevant_data):
    formatted_documents = ''
    for document in relevant_data:
        formatted_document += f"Title: {document['title']}\n"
        formatted_documents.append(formatted_document)
    return "\n".join(formatted_documents)
```
(2 mistakes — find both!)

---

## SECTION D — Big Picture (Tricky!)

**Q23.** Your friend says:
> "We can just give ALL the news data directly to the LLM every time. Why do we need `retrieve()`?"

Write a short reply explaining why `retrieve()` is important.

**Q24.** Look at this code and explain what each line does in simple words:
```python
def get_relevant_data(query, top_k=5):
    relevant_indices = retrieve(query, top_k)
    relevant_data = query_news(relevant_indices)
    return relevant_data
```

**Q25.** What is the main difference between RAG and a normal LLM call? Why was this assignment built using BBC News 2024 data specifically?

---

**Total: 25 Questions**
**All the best bro! You know everything — trust yourself!**
