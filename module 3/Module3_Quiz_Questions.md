# Module 3 - Vector Databases, ANN, Chunking & Query Techniques: Quiz Question Paper
### Saved from the Coursera quiz (10 questions) - use this when we study Module 3 step by step

---

**Q1.** What is the fundamental difference between k-nearest neighbors (kNN) and approximate nearest neighbors (ANN) algorithms in vector search?

- kNN is used for classification tasks while ANN is used for search tasks.
- kNN works with vectors while ANN works with other data structures.
- kNN calculates distances to all vectors while ANN uses optimized structures to avoid exhaustive search.
- kNN returns k results while ANN returns a variable number of results.

✅ CORRECT ANSWER: kNN calculates distances to all vectors while ANN uses optimized structures to avoid exhaustive search.

kNN is the "check every single vector" method: exact, but slow when you have millions. ANN builds a smart index (like HNSW) so it only checks a small part of the data. Both work on vectors and both return k results — the real difference is exhaustive vs. optimized.

---

**Q2.** A data scientist is implementing a vector database for a recommendation system that needs to handle millions of product embeddings. What should they understand about the results returned by the vector database?

- The vector database will always calculate distances to all vectors, just more efficiently.
- The results might not always be the exact nearest neighbors, but searches can be completed substantially faster.
- Query time will increase linearly as the number of vectors increases.
- The vector database still performs an exhaustive search, but only considers the vectors in the neighborhood of the query vector.

✅ CORRECT ANSWER: The results might not always be the exact nearest neighbors, but searches can be completed substantially faster.

This is the ANN trade-off: you give up a tiny bit of accuracy (recall) and get a HUGE speed gain. Linear query time and "calculates all distances" describe kNN, not ANN.

---

**Q3.** What is the key feature that distinguishes hybrid search from running vector and keyword searches independently?

- Hybrid search alternates between vector and keyword search methods depending on query complexity.
- Hybrid search assigns weights to results from both methods and combines their rankings using an alpha parameter.
- Hybrid search always adds semantic and keyword scores equally to compute a final document rank.
- Hybrid search uses vector search results and then filters them based on keyword matches.

✅ CORRECT ANSWER: Hybrid search assigns weights to results from both methods and combines their rankings using an alpha parameter.

`alpha` is a slider: alpha = 1 means pure vector search, alpha = 0 means pure keyword search, 0.5 is a mix. It's NOT always equal, and it doesn't alternate or just filter.

---

**Q4.** Why might using very large chunks in a vector database potentially reduce retrieval accuracy?

- Large chunks require more processing time to convert to vectors.
- Large chunks create vectors that average many different topics together, diluting specific concepts.
- Large chunks result in duplicate vectors being created for the same content, causing confusion during retrieval.
- Large chunks make it impossible for the database to build an effective index.

✅ CORRECT ANSWER: Large chunks create vectors that average many different topics together, diluting specific concepts.

One chunk = one vector. If the chunk talks about 5 topics, the vector becomes a blurry average of all 5 and matches none of them well. Smaller, focused chunks give sharper vectors.

---

**Q5.** A company has implemented query parsing in their retrieval system. Which expectation about this implementation is most realistic?

- Query parsing will sometimes provide benefits but at such a high computational cost that the tradeoff is not worth it.
- Query parsing will improve retrieval quality and works well in conjunction with other techniques like thoughtful chunking and re-ranking.
- Query parsing will help determine if a prompt should be processed by a cheaper bi-encoder or a more costly cross-encoder.
- Query parsing ensures only prompts that will result in a successful retrieval are processed by the system.

✅ CORRECT ANSWER: Query parsing will improve retrieval quality and works well in conjunction with other techniques like thoughtful chunking and re-ranking.

Query parsing (turning a messy question into clean filters/keywords) is one tool in the toolbox. It helps, and it works BEST together with chunking and re-ranking. It's not a gatekeeper and it doesn't choose between bi-encoder and cross-encoder.

---

**Q6.** Which of the following is a genuine limitation developers should consider when using Named Entity Recognition (NER) in query parsing?

- NER models can only process short queries under 50 words.
- NER models only extract entities from categories they're specifically configured to identify.
- NER models work only on formal, professionally written queries.
- NER models must be retrained for each new query type.

✅ CORRECT ANSWER: NER models only extract entities from categories they're specifically configured to identify.

If a NER model knows PERSON / PLACE / DATE, it will miss a category like "product model name" unless it's set up for it. The other options are made-up hard limits.

---

**Q7.** What is the most accurate characterization of bi-encoder models used in vector databases compared to cross-encoders used in reranking?

- Bi-encoders are a historical but ultimately primitive search technology that has since been replaced by the cross-encoder.
- Bi-encoders are effective at capturing general semantic similarity but miss some nuanced query-document interactions.
- Bi-encoders provide the same accuracy as cross-encoders but are restricted to initial retrieval due to design preference.
- Bi-encoders only work for exact keyword matching while cross-encoders handle semantic matching.

✅ CORRECT ANSWER: Bi-encoders are effective at capturing general semantic similarity but miss some nuanced query-document interactions.

Bi-encoder = encodes query and document SEPARATELY into vectors (fast, can pre-compute, good for searching millions). Cross-encoder = reads query + document TOGETHER (slower, more accurate, so used to re-rank the top few results). They work as a team, not a replacement.

---

**Q8.** In a hierarchical navigable small world (HNSW) algorithm, why does starting the search at the top layer with fewer vectors improve efficiency?

- The top layer contains only the most important documents in the collection.
- It allows making large navigational jumps to quickly identify the approximate neighborhood where the query belongs.
- It eliminates the need to build proximity graphs for lower layers.
- It reduces the total number of documents that need to be indexed.

✅ CORRECT ANSWER: It allows making large navigational jumps to quickly identify the approximate neighborhood where the query belongs.

Think of Google Maps: first zoom out (country → state), then zoom in (city → street). The top layer has few vectors with long-distance links = big jumps. Lower layers have more vectors = fine-tuning. Lower layers are still built, and all documents are still indexed.

---

**Q9.** What is a primary drawback of using semantic or LLM-based chunking in a RAG pipeline?

- These techniques tend to increase retrieval latency due to the higher number of chunks.
- These techniques rely too heavily on fixed chunk sizes that may not match content boundaries.
- Semantic and LLM-based chunking require extensive pre-processing and are computationally expensive.
- Semantic and LLM-based chunking produce lower retrieval quality than fixed-size chunking.

✅ CORRECT ANSWER: Semantic and LLM-based chunking require extensive pre-processing and are computationally expensive.

Semantic/LLM chunking needs to run embeddings or an LLM over your whole text to decide where to split — that costs time and money. Relying on fixed sizes is the drawback of FIXED-size chunking, not these.

---

**Q10.** In the HyDE (Hypothetical Document Embeddings) technique, what is the role of the hypothetical document?

- It is used to build filters for metadata search.
- It replaces the original prompt during semantic search.
- It improves LLM summarization during generation.
- It helps generate keywords for improved lexical search.

✅ CORRECT ANSWER: It replaces the original prompt during semantic search.

Steps: (1) LLM writes a fake/hypothetical answer to the question, (2) embed that fake answer, (3) search with it INSTEAD of the original question. A fake answer looks more like real documents than a short question does, so it matches better.

---

## Quick memory cheat-sheet

| Topic | One-line memory |
|---|---|
| kNN vs ANN | exact + slow vs approximate + fast |
| Hybrid search | `alpha` slider between vector and keyword |
| Chunk size | too big = blurry vector |
| Query parsing | helps, works best with chunking + re-ranking |
| NER limit | only finds the categories it's set up for |
| Bi-encoder vs Cross-encoder | fast + general vs slow + precise (re-rank) |
| HNSW | zoom out first, zoom in later |
| Semantic/LLM chunking | smart but expensive |
| HyDE | search with a fake answer instead of the question |
