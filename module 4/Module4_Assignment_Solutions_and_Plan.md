# Module 4 Assignment - Fashion Forward Hub ChatBot: Solutions + Study Plan
### Saved for later - we will go through each part step by step after the course is done

Paste ONLY the code that replaces the `None` lines between `### START CODE HERE ###` and `### END CODE HERE ###`.
Before running a graded cell, run the cells above it (imports, client, `FAQ_LAYOUT`, `values`) - the grader/test needs them.

---

## Big picture (the pipeline we built)

```
User message
   ↓
check_if_faq_or_product()        ← Exercise 1  (router: FAQ or Product?)
   ├── FAQ      → query_on_faq()              ← Exercise 2  (answer from the FAQ text only)
   └── Product  → decide_task_nature()        ← Exercise 3  (creative or technical?)
                  get_params_for_task()       ← Exercise 4  (temperature / top_p for that nature)
                  generate_metadata_from_query() ← Exercise 5 (LLM writes JSON filters: color, gender, price...)
                  → Weaviate near_text + metadata Filter → context → LLM answer
```

---

## Exercise 1 - `check_if_faq_or_product`

```python
    prompt = f"""Label the following instruction as an FAQ-related query or a product-related query.
Product-related queries are specific to product information or require using product details to answer. Products are clothes from a store.
An FAQ question addresses common inquiries (policies, returns, shipping, support, payment) and provides answers to help users find the information they need.

Examples:
Is there a refund for incorrectly bought clothes? Label: FAQ
Tell me about the cheapest T-shirts that you have. Label: Product
Do you have blue T-shirts under 100 dollars? Label: Product
I bought a T-shirt and I didn't like it. How can I get a refund? Label: FAQ
How can I contact the user support? Label: FAQ
Create a look suitable for a wedding party. Label: Product

Return only one of the two labels: FAQ or Product.
Instruction: {query}"""

    kwargs = generate_params_dict(prompt, temperature=0, max_tokens=1)

    response = generate_with_single_input(**kwargs)

    label = response['content'].strip()
    if label not in ['FAQ', 'Product']:
        label = None
```

Why: few-shot examples (a few Q → Label pairs) teach the LLM the task. `temperature=0` = no randomness. `max_tokens=1` = only ONE token comes back, so we get just the label. If the answer is not exactly FAQ/Product we return `None` so `answer_query()` can handle it.
(If you ever see `FA` instead of `FAQ`, the label got cut - raise `max_tokens` to 3.)

---

## Exercise 2 - `query_on_faq`

```python
    prompt = f"""You will be provided with an FAQ for a cloth store.
Answer the instruction based on it. You might use more than one question and answer to make your answer. Only answer the question and do not mention that you have access to a FAQ.
<FAQ>
PROVIDED FAQ: {FAQ_LAYOUT}
</FAQ>
Question: {query}"""

    kwargs = generate_params_dict(prompt, **kwargs)
```

Why: we paste the whole FAQ text into the prompt (that's the "Augment" step) and tell the LLM to answer ONLY from it = fewer hallucinations. The function returns the `kwargs` dict, NOT the answer (the answer is generated later by `generate_with_single_input(**kwargs)`).

---

## Exercise 3 - `decide_task_nature`

```python
    prompt = f"""Decide if the following query is a query that requires creativity (creating, composing, making new things, suggesting looks or matching items) or technical (information about products, prices, availability, etc.). Label it as creative or technical.

Examples:
Give me suggestions on a nice look for a nightclub. Label: creative
What are the blue dresses you have available? Label: technical
Give me three T-shirts for summer. Label: technical
Give me a look for attending a wedding party. Label: creative
I have a red shirt and I want a suggestion on an accessory to match with it. Label: creative
What is the most expensive jacket in your catalogue? Label: technical

Query to be analyzed: {query}. Only output one token: the label."""

    kwargs = generate_params_dict(prompt, temperature=0, max_tokens=1)

    response = generate_with_single_input(**kwargs)

    label = response['content'].strip().lower()
```

Why: same trick as Exercise 1. The tricky example is "I have a green dress ... suggestion on an accessory" = creative (it sounds like a product question, but it asks for a suggestion).

---

## Exercise 4 - `get_params_for_task`

```python
    PARAMETERS_DICT = {
        "creative": {"top_p": 0.9, 'temperature': 1.0},
        "technical": {'top_p': 0.7, 'temperature': 0.3}
    }

    if task == 'technical':
        param_dict = PARAMETERS_DICT['technical']
    elif task == 'creative':
        param_dict = PARAMETERS_DICT['creative']
    else:
        # Fallback: conservative (low randomness)
        param_dict = {'top_p': 0.7, 'temperature': 0.3}
```

Why: technical questions (prices, facts) need SAFE, repeatable answers = low temperature. Creative questions (build a look) can be more random = higher temperature. Keep temperature under 1.3 and top_p at most 1. Unknown task → safe default.

---

## Exercise 5 - `generate_metadata_from_query`

Remember: inside an f-string, a literal `{` or `}` must be written as `{{` and `}}`. Only `{values}` and `{query}` stay single.

```python
    prompt = f"""A query will be provided. Based on this query, a vector database will be searched to find relevant clothing items.
Generate a JSON object containing useful metadata to filter products for this query.
The possible values for each feature are given in the following JSON: {values}

Provide a JSON containing the features that best match the query (values should be in lists, multiple values possible).
If a price range is mentioned, include a price key specifying the range (between values, greater than, or less than).
Return only the JSON, nothing else. The price key must be a JSON object with "min" and "max" values (use 0 if no lower bound, and "inf" if no upper bound).
Always include the following keys: gender, masterCategory, articleType, baseColour, price, usage, and season.
If no price is specified, set min = 0 and max = inf.
Include only values present in the JSON above.

Example of expected JSON:

{{
  "gender": ["Women"],
  "masterCategory": ["Apparel"],
  "articleType": ["Dresses"],
  "baseColour": ["Blue"],
  "price": {{"min": 0, "max": "inf"}},
  "usage": ["Formal"],
  "season": ["All seasons"]
}}

Query: {query}"""

    kwargs = generate_params_dict(prompt, temperature=0, max_tokens=1500)

    response = generate_with_single_input(**kwargs)

    content = response['content']
```

Why: we give the LLM the list of ALLOWED values (`values`), ask for JSON only, and show an example of the exact format. `max_tokens=1500` so the JSON is not cut in half (a cut JSON cannot be parsed). Later `parse_json_output()` turns the text into a Python dict and `get_filter_by_metadata()` turns that into Weaviate `Filter` objects.

---

## Study plan - what we will learn step by step later

| # | Topic | Where it shows up | Connects to |
|---|---|---|---|
| 1 | LLM router (classify the intent first) | Exercise 1 | agentic workflows, router LLM (Module 4 quiz Q10) |
| 2 | Few-shot prompting | Ex 1, 3 | quiz Q5: few-shot = number of examples |
| 3 | Low temperature + max_tokens=1 for labels | Ex 1, 3 | quiz Q3 |
| 4 | Grounding the answer in the FAQ text | Ex 2 | hallucinations (quiz Q4), RAG's "A" step |
| 5 | Temperature / top_p chosen per task | Ex 4 | quiz Q3 |
| 6 | Make the LLM output JSON + parse it safely | Ex 5, `parse_json_output` | double braces `{{ }}` in f-strings |
| 7 | LLM-generated metadata filters -> Weaviate `Filter` | `get_filter_by_metadata` | Module 3 Lab 1 filters, hybrid + metadata |
| 8 | Fallback: remove the least important filters when results are few | `get_relevant_products_from_query` | real-world retrieval robustness |
| 9 | Context building + final answer | `generate_items_context`, `query_on_products` | the full RAG pipeline from Module 1 |
| 10 | Wrap everything with error handling | `answer_query` | `try / except`, returning a safe default |

Mistakes to watch for (from our history): forgetting `return`, passing arguments positionally instead of by name, leaving `___` or `None` placeholders, and not re-running the graded cell after editing it.
