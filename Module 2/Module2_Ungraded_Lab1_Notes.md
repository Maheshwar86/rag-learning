# Module 2 - Ungraded Lab 1: Vector Embeddings in RAG (notes)
### Read-and-run lab, no questions to answer. Notes for studying later.
(The notebook `C1M2_Ungraded_Lab_1.ipynb` was downloaded into the `module 4` folder by mistake - it belongs in `Module 2`.)

## 1. The idea
An embedding model turns text into a vector (a point on a "meaning map"). Similar meaning = points close together.
Framework: (1) embed the query and the documents, (2) measure closeness with a metric, (3) sort and keep the top few.

## 2. Two ways to measure closeness

| Metric | What it measures | Best result is | Sort order |
|---|---|---|---|
| Cosine similarity | the ANGLE between two vectors | close to 1 | descending |
| Euclidean distance | the straight-line DISTANCE | small | ascending |

Example from the lab: v1 = [1, 2], array = [[3, 2], [5, 6]]
- Cosine: closest is the SECOND vector ([5, 6]: 0.974 vs 0.868).
- Euclidean: closest is the FIRST vector ([3, 2]: 2.0 vs 5.66).
They disagree because cosine ignores how long the vectors are and only looks at direction.

## 3. The embedding model
- `BAAI/bge-base-en-v1.5` through `SentenceTransformer`, output = 768 numbers per sentence. `model.encode("text")` gives one vector; `model.encode([list])` gives one vector per item.
- Words with related meaning ("apple" and "fruit") score closer than unrelated ones ("apple" and "car").
- Surprise in the lab: for "Suggest to me great places to visit in Asia", Kyoto did NOT rank first. Embeddings learn from words that appear together in training data, so generic travel sentences can beat a factually better match.
- PCA (the widget) squashes 768 dimensions down to 2 so you can plot and see the clusters.

## 4. Input size limit
- The model reads only the first 512 tokens. Everything after is ignored.
- Proof in the lab: embedding the whole big text and only its first 3000 characters gave the EXACT same vector.
- This is why we need chunking (Module 3).

## Where this shows up later
- Semantic search in the Module 2 assignment and in `rag_system2.py` (our planned `semantic_search_retrieve()` uses the same idea with `all-MiniLM-L6-v2`).
- Module 3 chunking lab and quiz Q4 (big chunks = blurry vectors).
