# Module 1 Assignment - Introduction to RAG Systems: Solutions
### Written by Mahesh himself. Taken from `C1M1_Assignment done.ipynb` (both unit tests show "All tests passed!").

The assignment has two graded functions.

## Function 1 - `get_relevant_data`

```python
    relevant_indices = retrieve(query, top_k)

    relevant_data = query_news(relevant_indices)
```

Why: the library idea. `retrieve()` finds which articles match (their index numbers), `query_news()` fetches the full articles for those numbers.

## Function 2 - `format_relevant_data`

```python
    formatted_documents = []

    for document in relevant_data:
        formatted_document = (f"""

        the news is based on this Title:  {document['title']} and here url : {document['url']} and this news published at {document['published_at']} date
        Now here Full Description
        {document['description']}

        """)

        formatted_documents.append(formatted_document)

    # after the END marker (already in the template):
    return "\n".join(formatted_documents)
```

Why: turn each article (a dictionary) into readable text and put all of them in one string for the prompt (the "Augment" step).

Mistakes we fixed on the way (from our history): `.append()` must be INSIDE the for loop, `.join()` must join the LIST, and the function must `return`.
