# Module 5 Assignment - Improving the RAG System (cost, tokens, speed, tracing): Solutions + Study Plan
### Saved for later - we will go through each part step by step after the course is done

Paste ONLY the code that replaces the `None` lines between `### START CODE HERE ###` and `### END CODE HERE ###`.
There are 4 graded exercises. Phoenix tracing and the cost-per-token setup (section 1.4) are NOT graded.

## Big picture

Module 4's chatbot works, but it is EXPENSIVE and SLOW (~1200 tokens for a FAQ, ~1500 tokens just to build filters for a product query).
Module 5 makes it cheaper and faster with a `simplified=True` mode:

| Step | Before (simplified=False) | After (simplified=True) | Exercise |
|---|---|---|---|
| FAQ or Product? | long prompt, 8 examples | short prompt, < 180 tokens | 1 |
| Answer a FAQ | paste the WHOLE FAQ in the prompt (~1200 tokens) | semantic search, only the top 5 FAQ items (< 500 tokens) | 2 |
| Creative or technical? | long prompt | short prompt, < 150 tokens, 80% accuracy | 3 |
| Find products | LLM writes JSON filters first (~1500 tokens) | one semantic search, 0 LLM tokens | 4 |

---

## Exercise 1 - `check_if_faq_or_product` (simplified prompt, < 180 tokens in total)

Replace `PROMPT = None` in the `else:` branch:

```python
        PROMPT = f"""Classify the clothing-store query as FAQ (policies, returns, shipping, contact) or Product (items, prices, colors, outfit ideas).
Examples:
Is there a refund for wrong clothes? FAQ
Do you have blue T-shirts under 100 dollars? Product
Give me ideas for a sunny look. Product
How can I contact you by phone? FAQ
Answer with one word.
Query: {query}"""
```

Why: fewer examples + shorter instructions = fewer tokens, but we keep one tricky example of each kind ("ideas for a sunny look" sounds general but it is a Product query; "contact you by phone" is an FAQ). Always keep `{query}` in the prompt.

---

## Exercise 2 - `query_on_faq` (simplified = semantic search on the FAQ collection)

Replace `results = None`:

```python
                results = faq_collection.query.near_text(query=query, limit=5)
```

Why: instead of pasting all 25 FAQ answers, we only fetch the 5 most similar ones using the vector database (Module 3). The rest of the function already turns them into the prompt. Result: far fewer tokens, same correct answer.

---

## Exercise 3 - `decide_task_nature` (simplified prompt, < 150 tokens, >= 80% accuracy)

Replace `PROMPT = None` in the `else:` branch:

```python
        PROMPT = f"""creative = asks to suggest a look or items that match/go with something.
technical = asks to find or list products, prices, colors.
Examples:
Look for a wedding party. Label: creative
Jeans under 50 dollars? Label: technical
What goes with my green T-shirt? Label: creative
Show me three summer T-shirts. Label: technical
Query: {query}. Only output one lowercase word: creative or technical."""
```

Why: the first version of this prompt (4 longer examples, no definitions) FAILED the test ("Error count = 3, expected <= 2"). This version gives a one-line DEFINITION of each class plus short examples, so the model decides by rule instead of guessing from examples. It also stays well under the 150-token limit (about 110 tokens for the longest query). The label must come back exactly `creative` or `technical` (lowercase), so the examples use lowercase labels and the prompt asks for a lowercase word.
If it still fails: run the example cell, look at which queries are RED, and add one short example that looks like that query (drop an easy example to stay under 150 tokens).

---

## Exercise 4 - `get_relevant_products_from_query` (simplified = no metadata filters)

Replace `results = None` (inside `if simplified:`, keep the indentation):

```python
            results = products_collection.query.near_text(query=query, limit=20)
```

Why: skip the expensive "LLM writes JSON filters" step completely. Just one semantic search with 20 results (same limit as before). It uses 0 LLM tokens, which is why the function returns `results.objects, 0`.

---

## Notes

- Not graded and not ours to fix: in `get_params_for_task` the course code uses two separate `if` blocks, so a `technical` task falls into the final `else` and gets the fallback parameters. Leave it as is for the assignment.
- Total tokens = input + output. That is why shorter prompts (and fewer retrieved items) directly mean lower cost.

## Study plan - what we will learn step by step later

| # | Topic | Where it shows up | Connects to |
|---|---|---|---|
| 1 | Cost = tokens x price per token | section 1.4, `total_tokens` | quiz Q7 (reduce LLM cost) |
| 2 | Shorter prompts keep accuracy if examples are chosen well | Ex 1, 3 | few-shot prompting |
| 3 | Retrieve only what you need (top-k from a vector DB, not the whole FAQ) | Ex 2 | Module 3 semantic search, quiz Q7/Q8 |
| 4 | Skip steps that cost an LLM call | Ex 4 | router / agentic ideas, quiz Q9 (latency) |
| 5 | Tracing with Phoenix (spans, inputs/outputs, token counts) | `tracer.start_as_current_span` | quiz Q4/Q5 (observability, tracing) |
| 6 | Trade-off: cost vs speed vs quality | the whole assignment | evaluation (quiz Q1-Q3) |
