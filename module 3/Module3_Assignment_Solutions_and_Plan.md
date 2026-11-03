# Module 3 Assignment - RAG with a Vector Database (Weaviate + BBC News): Solutions + Study Plan
### Saved for later - we will go through each part step by step after the course is done

Replace ONLY the `response = None` lines (Exercise 5 also has `reranker = None`) between `### START CODE HERE ###` and `### END CODE HERE ###`.
Inside each function use the `collection` PARAMETER (not a global variable) and pass arguments by NAME.

## Big picture

One BBC News collection in Weaviate, four ways to search it:

| Exercise | Function | Weaviate method | Idea |
|---|---|---|---|
| 1 | `filter_by_metadata` | `fetch_objects` + `Filter` | exact attribute match, no meaning (Module 2: metadata filtering) |
| 2 | `semantic_search_retrieve` | `near_text` | vector / meaning search |
| 3 | `bm25_retrieve` | `bm25` | keyword search |
| 4 | `hybrid_retrieve` | `hybrid` + `alpha` | keyword + vector combined (alpha 1 = pure vector, 0 = pure keyword) |
| 5 | `semantic_search_with_reranking` | `near_text` + `Rerank` | re-score the top results with a cross-encoder |

---

## Exercise 1 - `filter_by_metadata`

```python
    response = collection.query.fetch_objects(
        filters=Filter.by_property(metadata_property).contains_any(values),
        limit=limit
    )
```

## Exercise 2 - `semantic_search_retrieve`

```python
    response = collection.query.near_text(query=query, limit=top_k)
```

## Exercise 3 - `bm25_retrieve`

```python
    response = collection.query.bm25(query=query, limit=top_k)
```
Expected output looks odd (a Killer Mike article for a Taylor Swift query) - that is correct. BM25 matches common words like "the" and "about" literally.

## Exercise 4 - `hybrid_retrieve`

```python
    response = collection.query.hybrid(query=query, alpha=alpha, limit=top_k)
```

## Exercise 5 - `semantic_search_with_reranking`

Keep the `if rerank_query is None:` lines. Replace the two `None` lines:

```python
    reranker = Rerank(prop=rerank_property, query=rerank_query)

    response = collection.query.near_text(query=query, limit=top_k, rerank=reranker)
```
The notebook hint says `Reranker(...)` but the imported class is `Rerank`. `Reranker` gives a NameError.

---

## Mistakes we hit on the way

- Running the skeleton with the `___` placeholders still in it. In Jupyter `___` is a real variable (output from 3 cells ago), which gave "contains_any must have at least one value".
- Not re-running the graded cell after editing it.
- Passing arguments by position instead of by name.

## Study plan - what we will learn step by step later

| # | Topic | Where it shows up | Connects to |
|---|---|---|---|
| 1 | What a vector database is (collection, properties, vectorizer) | Lab 1 | Module 2 embeddings |
| 2 | kNN vs ANN and HNSW (zoom out, then zoom in) | lectures, quiz Q1/Q2/Q8 | why vector search is fast |
| 3 | Metadata filters with `Filter.by_property` | Ex 1, Lab 1 | Module 2 metadata filtering |
| 4 | Semantic vs BM25 vs hybrid + `alpha` | Ex 2-4 | Module 2 BM25 + RRF |
| 5 | Reranking with a cross-encoder | Ex 5, quiz Q7 | bi-encoder vs cross-encoder |
| 6 | Chunking: fixed size, overlap, by paragraph, mixed | Lab 2, quiz Q4/Q9 | small = precise, big = blurry |
| 7 | Query parsing, NER, HyDE | lectures, quiz Q5/Q6/Q10 | smarter queries |
