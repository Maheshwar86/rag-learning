import os
from dotenv import load_dotenv
from openai import OpenAI
from ai_news_data import AI_NEWS
import bm25s

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/"
)


# ---- BM25 setup (one-time indexing, done once when the file runs) ----
corpus = [f"{news['title']} {news['description']}" for news in AI_NEWS]
BM25_RETRIEVER = bm25s.BM25(corpus=corpus)
tokenized_corpus = bm25s.tokenize(corpus)
BM25_RETRIEVER.index(tokenized_corpus)


def bm25_retrieve(query, top_k=2):
    tokenized_query = bm25s.tokenize(query)        # hint: bm25s.tokenize(), same as corpus was tokenized above
    results, scores =BM25_RETRIEVER.retrieve(tokenized_query , k=top_k)         # hint: BM25_RETRIEVER.retrieve(...), pass tokenized_query and k=top_k
    results =results[0]                 # hint: results is a 2D list (one row per query) — grab the first row
    top_k_indices = [corpus.index(doc) for doc in results]          # hint: for each doc text in results, find its position using corpus.index(doc)
    return top_k_indices


print(bm25_retrieve('tell claude 4'))

def query_news(top_k_indices):
    return [AI_NEWS[i] for i in top_k_indices]


print(query_news(bm25_retrieve('tell me about claude')))

def news_relevant_data(query , top=2):
    relevant_numbers = bm25_retrieve(query,top)
    relevant_documents = query_news(relevant_numbers)
    return relevant_documents

def news_format(relevant_documents):
    formted_datas = []
    for document in relevant_documents:
        formated_document = f""" 

        Title : {document['title']}
        Description : {document['description']}
        Published_at : {document['published_at']}
        Url : {document['url']}

        """
        formted_datas.append(formated_document)
    return "\n".join(formted_datas)

print(news_format(news_relevant_data('tell me about claude')))

def genrate_final_prompt(query,formated_data):
    prompt = f"""  

    Answer the question using below data

    News : 
    {formated_data}

    Question : {query}
    """
    return prompt


def llm_call(prompt):
    output = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {'role':'user','content':prompt}
        ]
    )
    return output.choices[0].message.content

query = "tell me about maheswar reddy"
data = news_relevant_data(query)
formated = news_format(data)
prompt = genrate_final_prompt(query,formated)
answer = llm_call(prompt)
print(answer)