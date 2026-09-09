# Lab 1 - Python Refresher: Question Paper
### Completed and Corrected!

---

## SECTION A - Theory Questions

**Q1.** What is a List in Python? Give one real life example.

⚠️ YOUR ANSWER: in list real world example is cycle park in japan in that every cycle list type all going step by step if new cycle coming mean last adding not puting random
✅ CORRECT ANSWER: A list is an ordered collection of items in Python. Items are stored in sequence and you can add, remove or access them. Real life example: cycle park — cycles parked in a row, new cycle added at the end. (Your example was correct! Just needed the definition.)

---

**Q2.** Does `.append()` add item at the beginning or end of a list?

✅ YOUR ANSWER: .append() adding list end of list not beginning — CORRECT!

---

**Q3.** What is the difference between `.append()` and `.insert()`?

⚠️ YOUR ANSWER: l1.insert('Mango', 1) — syntax was WRONG
✅ CORRECT ANSWER:
- .append() → always adds at the END
- .insert() → adds at any position you choose
- Correct syntax: l1.insert(1, 'Mango') → INDEX first, VALUE second!
```python
l1.insert(1, 'Mango')   # ✅ index first, value second
l1.insert('Mango', 1)   # ❌ wrong order
```

---

**Q4.** What is a Dictionary in Python? What are keys and values?

⚠️ YOUR ANSWER: partially correct
✅ CORRECT ANSWER: A dictionary stores data in key:value pairs. Keys are labels (like column names), values are the actual data stored against that label.
```python
person = {'name': 'Alice', 'age': 25}
# 'name' and 'age' are KEYS (labels)
# 'Alice' and 25 are VALUES (data)
```

---

**Q5.** What is the difference between looping with `.items()` and looping without `.items()`?

✅ YOUR ANSWER: .items() gives keys and values both, without .items() only keys come — CORRECT!

---

**Q6.** What is an f-string? Why is it better than normal string joining?

✅ YOUR ANSWER: CORRECT! f-string is cleaner, easier to read than + joining.

---

**Q7.** Inside an f-string, which quotes do you use for the f-string and which for dictionary keys?

✅ YOUR ANSWER: f"hello {person['name']}" — CORRECT! Double quotes outside, single quotes for keys inside.

---

## SECTION B - Predict the Output

**Q8.** Output of the list code?

✅ YOUR ANSWER: ['RAG', 'awesome', '!'] — CORRECT!

---

**Q9.** Output of list comprehension?

⚠️ YOUR ANSWER: "its a square" — incomplete, no actual output given
✅ CORRECT ANSWER:
- range(5) = 0, 1, 2, 3, 4
- x**2 = 0, 1, 4, 9, 16
- Output: [0, 1, 4, 9, 16]

---

**Q10.** Output of dictionary loop?

⚠️ YOUR ANSWER: {'name':'Alice', 'age':25} — WRONG
✅ CORRECT ANSWER: .items() with a loop prints EACH key and value on separate lines:
```
name Alice
age 25
```
Not the whole dictionary on one line!

---

**Q11.** Output of f-string print?

⚠️ YOUR ANSWER: "my name is Ravi and iam 22 years old." — almost but wrong capitalization
✅ CORRECT ANSWER: Python prints EXACTLY what is in the string:
```
My name is Ravi and I am 22 years old.
```
Capital M, capital I, space between "I am"

---

## SECTION C - Coding Questions

**Q12.** Create list with 3 fruits, add mango, remove first, print final.

⚠️ YOUR ANSWER: Created 4 fruits (goa is not a fruit!), printed twice instead of once at end
✅ CORRECT ANSWER:
```python
fruits = ['banana', 'apple', 'orange']   # 3 fruits only
fruits.append('mango')
fruits.remove('banana')
print(fruits)                             # print ONCE at the end
# Output: ['apple', 'orange', 'mango']
```

---

**Q13.** List comprehension for numbers 1 to 20 divisible by 3.

⚠️ YOUR ANSWER: range(20) — WRONG, starts from 0 and misses 20
✅ CORRECT ANSWER:
```python
num = [x for x in range(1, 21) if x % 3 == 0]
print(num)
# Output: [3, 6, 9, 12, 15, 18]
```
range(1, 21) → starts at 1, ends at 20 (inclusive)

---

**Q14.** Dictionary with student keys, print only values using .items()

⚠️ YOUR ANSWER: print({value}) — WRONG, {value} creates a SET not prints value!
✅ CORRECT ANSWER:
```python
student = {
    'name': 'Mahesh',
    'age': 23,
    'course': 'mca'
}
for keys, value in student.items():
    print(value)       # ✅ just value, no curly braces!
# Output:
# Mahesh
# 23
# mca
```

---

**Q15.** Print each student using f-string.

⚠️ YOUR ANSWER: .join() and print() were INSIDE the loop — causes repeated output, format wrong
✅ CORRECT ANSWER:
```python
students = [
    {'name': 'Ravi', 'marks': 85},
    {'name': 'Priya', 'marks': 92},
    {'name': 'Kiran', 'marks': 78}
]
stu = []
for x in students:
    line = f"Student: {x['name']}, Marks: {x['marks']}"
    stu.append(line)
per_str = "\n".join(stu)   # OUTSIDE the loop!
print(per_str)              # OUTSIDE the loop!
```
Key fix: .join() and print() must be OUTSIDE the loop!

---

## SECTION D - Bonus

**Q16.** What does this print and WHY?

⚠️ YOUR ANSWER: Said [1,2,3,4] — WRONG
✅ CORRECT ANSWER: Prints None!
```python
l = [1, 2, 3]
result = l.append(4)   # .append() returns NOTHING (None)!
print(result)          # prints: None
```
.append() changes the list directly but returns None. If you want the list, print l not result!

---

**Q17.** Fix the error in the f-string code.

✅ YOUR ANSWER: Changed outer quotes to double quotes — CORRECT!
```python
person = {'name': 'Alice'}
print(f"Name: {person['name']}")   # ✅
```

---

**Total: 17 Questions**
**Your Score: 8/17 → After revision keep these notes for future reference!**
