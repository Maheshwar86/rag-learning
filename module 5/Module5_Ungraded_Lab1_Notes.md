# Module 5 - Ungraded Lab 1: Tracing a RAG System with Phoenix (notes)
### Read-and-run lab, no questions to answer. Notes for studying later.

## 1. Telemetry basics (OpenTelemetry)
- **Span** = one operation (start time, end time, attributes, events, status OK/ERROR). Example: one `retrieve()` call.
- **Trace** = all the spans that belong to ONE request, from the question to the final answer.
- Toy pipeline: `retrieve -> format_documents -> augment_prompt -> generate`, wrapped by a parent span `rag_pipeline`.
- Running it with `fail=True` shows an ERROR span, so you can see WHICH step broke.
- With a plain `ConsoleSpanExporter` the raw output is long and hard to read -> that is why we use Phoenix.

## 2. Phoenix (visual tracing tool)
- `px.launch_app()` starts a UI on `localhost:6006`; on Coursera use the link from `utils.make_url()`.
- `register(project_name=..., endpoint="http://127.0.0.1:6006/v1/traces")` gives a tracer.
- Retriever span: `tracer.start_as_current_span("...", openinference_span_kind='retriever')` and `span.set_input(query)`.
- **Chains**: put `@tracer.chain` above a function and it is traced automatically.
- Failed runs show up in red in the UI.
- Gotcha: `utils.restart_kernel()` (cell 30) restarts the kernel ON PURPOSE. After it, continue from section 4 (re-run the imports). Also never run the `kill_processes_on_ports` cell twice.

## 3. Tracing a real pipeline with Weaviate (FAQ collection)
- `register(..., auto_instrument=True)` automatically traces every OpenAI-compatible LLM call (prompt, answer, token counts).
- Retriever: Weaviate `near_text(query, limit=5)`; each retrieved document is saved as span attributes (id, metadata, content).
- `format_context` and `create_prompt` are `@tracer.chain` functions.
- LLM call uses the `openai` library with a `base_url` pointing to any OpenAI-compatible endpoint (Together here). That is the same pattern as your DeepSeek client (`base_url="https://api.deepseek.com/"`).
- Run 2 questions ("Can I get a refund or exchange for another shirt?", "What are your working hours?") and then inspect the traces in the Phoenix UI.

## Why it matters (Module 5 quiz)
- Q4/Q5: observability = trace each query through every component to find where a bad answer came from.
- The Module 5 assignment uses the same tracer to track tokens/cost of each step (cost per token setup in section 1.4).
