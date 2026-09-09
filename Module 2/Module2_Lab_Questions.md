# Module 2 - Retrieval Metrics & Search Fundamentals: Quiz Question Paper
### Completed and Corrected!

---

**Q1.** What is the primary function of metadata filtering in a retrieval system?

✅ CORRECT ANSWER: To match specific document attributes against strict query criteria.

Metadata filtering checks fixed attributes (date, author, tags) against exact criteria — like a database `WHERE` clause. It's not analyzing meaning or converting to vectors — that's semantic search's job.

---

**Q2.** What fundamental limitation makes metadata filtering less effective than other retrieval methods for comprehensive document discovery?

✅ CORRECT ANSWER: It evaluates only document metadata while ignoring the actual content.

Metadata filtering narrows down results but never looks at what the document actually SAYS, only its tags/attributes — that's why it's "useless alone" for real search.

---

**Q3.** When text is represented as a "Bag of Words" in keyword search, what single aspect of the original text is preserved?

✅ CORRECT ANSWER: The number of times each word appears in the text.

Example: "pizza" = 2, "oven" = 1. Word ORDER is thrown away completely — only the count (frequency) of each word survives.

---

**Q4.** What primary capability defines keyword search when implemented in retrieval systems?

✅ CORRECT ANSWER: Matching documents that contain the exact words found in the query.

Keyword search scores documents by whether they contain the SAME words as your query — exact text matches, not meaning, not metadata tags.

---

**Q5.** What fundamental limitation of keyword search do embedding models specifically address in retrieval systems?

✅ CORRECT ANSWER: The inability to connect semantically similar words or concepts.

Example: "happy" vs "glad" — keyword search sees these as totally unrelated (different letters), even though they mean the same thing. Embeddings fix exactly this gap.

---

**Q6.** How do embedding models determine the vector space positions of words during their training process?

✅ CORRECT ANSWER: By iteratively adjusting positions based on training data made up of "positive" and "negative" word pairs.

Contrastive training: "Good Morning"+"Hello" = positive pair (pulled closer), "Good Morning"+"noisy trombone" = negative pair (pushed apart). Repeats thousands of times, gradually shaping the vector space — not predefined by linguists or dictionaries.

---

**Q7.** In which specific situation would keyword search likely perform better than semantic search in a retrieval system?

✅ CORRECT ANSWER: When searching for precise technical terminology or product codes.

Keyword search guarantees exact matches. A product code like "RTX-4090" needs EXACT matching — semantic search might substitute something "similar" and miss the precise code entirely.

---

**Q8.** What is the primary function of Reciprocal Rank Fusion (RRF) in a hybrid search system?

✅ CORRECT ANSWER: To merge ranked lists from different search methods mathematically.

RRF example: keyword rank 2nd (0.5 pts) + semantic rank 10th (0.1 pts) = 0.6 total score. It combines two separate ranked lists into one final ranking using the reciprocal-of-rank math.

---

**Q9.** In retrieval system evaluation, what is the primary purpose of using a Top-K cutoff when calculating metrics like precision or recall?

✅ CORRECT ANSWER: It helps standardize evaluation by focusing on the top-ranked results, which are typically the most useful for downstream tasks.

Since an LLM only gets fed a handful of documents (context limits), what matters is quality at the TOP, not documents ranked #200 — Top-K cutoff focuses metrics on what's actually usable.

---

**Q10.** Cooking website scenario — short recipe cards (mention "chocolate" 5% of words) vs long cookbook chapters (mention "chocolate" 0.5% of words but 30 total times). Which algorithm fixes short documents unfairly dominating results — TF-IDF or BM25?

✅ CORRECT ANSWER: BM25, because it penalizes long documents less aggressively than TF-IDF.

TF-IDF = "Long Doc = Heavy Penalty (too aggressive)" vs BM25 = "Long Doc = Smaller Penalty (document length normalization)." The 10-page chapters are being unfairly buried by TF-IDF's harsh length penalty — BM25's fairer normalization fixes that. (Not because BM25 "favors" long docs — it just doesn't unfairly punish them.)

---

**Total: 10 Questions**

---

## KEY THINGS TO REMEMBER (Module 2):

| Concept | Key Point |
|---|---|
| Metadata Filtering | Rigid criteria on attributes (date/author/tags), ignores content, can't rank |
| Keyword Search / Bag of Words | Exact word matches, order ignored, only frequency counted |
| TF-IDF | Rewards rare keywords, but penalizes long documents too aggressively |
| BM25 | Refined TF-IDF — term frequency saturation + fairer document length normalization |
| Semantic Search / Embeddings | Converts text to vectors capturing MEANING, fixes synonym problem |
| Embedding Training | Contrastive learning — positive pairs pulled close, negative pairs pushed apart, repeated |
| Hybrid Search | Combines keyword + semantic + metadata filtering for best results |
| Reciprocal Rank Fusion (RRF) | Merges multiple ranked lists using 1/rank scoring |
| Precision@K | Relevant Retrieved / Total Retrieved — measures QUALITY |
| Recall@K | Relevant Retrieved / Total Relevant in corpus — measures COMPLETENESS |
| Top-K cutoff | Metrics focus on top-ranked results since that's what's actually usable downstream |
