# Module 4 - Ungraded Lab 2: Prompt Engineering (notes)
### Read-and-run lab, no questions to answer. Notes for studying later.

## 1. Text classification with an LLM
Turn the LLM into a classifier (here: "nutritional" or "outfit"). Recipe:
1. Be precise: say exactly what to output ("Answer only one single word").
2. Add examples with the expected label.
3. Add edge examples the LLM may get wrong (e.g. "Best weight loss products that are stylish" -> Nutritional, "Athletic wear that boosts performance" -> Outfit).
4. Check the output in code (the next step may expect exactly one of the labels, not a sentence).

The lab compares `result == expected_label` (exact match) and prints green/red. `max_tokens = 2` keeps the reply short.

## 2. Parameters chosen by the nature of the task
Pipeline: `decide_if_technical_or_creative(query)` -> pick parameters -> generate the answer.

| Task | temperature | top_p | Why |
|---|---|---|---|
| technical | 0 | 0.1 | precise, repeatable |
| creative | 1.1 | 0.4 | more variety |
| unknown | 0.5 | 0.5 | neutral fallback |

- temperature = how random the next word choice is.
- top_p = only consider the smallest group of likely words whose probabilities add up to top_p.
- Always have an `else` for when the LLM returns something unexpected.

## 3. Making the LLM output JSON
- Old-fashioned way: a long prompt that lists devices/actions and shows example JSON. Inside an f-string the JSON braces must be doubled `{{ }}`. Low temperature (0.4) and top_p (0.1). Tell it to ALWAYS output a list.
- Better way (structured output): define a Pydantic schema (`BaseModel` + `Field(description=...)`), then pass
  `response_format={"type": "json_schema", "schema": VoiceNote.model_json_schema()}`
  together with `messages` (a `system` and a `user` message). The reply is guaranteed JSON -> `json.loads(result['content'])`.

## Where this shows up in the Module 4 assignment
- Section 1 -> Exercise 1 (FAQ or Product router)
- Section 2 -> Exercises 3 and 4 (creative or technical + parameters)
- Section 3 -> Exercise 5 (JSON metadata filters)
