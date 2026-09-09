import os
from dotenv import load_dotenv
from openai import OpenAI
from ai_news_data import AI_NEWS

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/"
)


# output =  client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {'role':'user','content':'Hello Good morning bro '}
#     ]
# )

# print(output.choices[0].message.content)

def retrieve(query , top):
    query_words = query.lower().split()
    scores = []
    for i , news in enumerate(AI_NEWS):
        text = f"{news['title']} {news['description']}".lower()
        score = 0
        for word in query_words:
            if word in text:
                score+=1
        scores.append([i,score])
    scores.sort(key=lambda x:x[1],reverse=True)
    top_indices = [item[0] for item in scores[:top]]
    return top_indices
# print(retrieve('tell claude 4'))

# def query_news(top_indices):
#     return [AI_NEWS[i] for i in top_indices]

# #print(query_news(retrieve('tell claude 4')))


# def news_relevant_data(query , top=5):
#     relevant_numbers = retrieve(query,top)
#     relevant_documents = query_news(relevant_numbers)
#     return relevant_documents

# def news_format(relevant_documents):
#     formted_datas = []
#     for document in relevant_documents:
#         formated_document = f""" 

#         Title : {document['title']}
#         Description : {document['description']}
#         Published_at : {document['published_at']}
#         Url : {document['url']}

#         """
#         formted_datas.append(formated_document)
#     return "\n".join(formted_datas)

# #print(news_format(news_relevant_data('tell claude 4')))

# def genrate_final_prompt(query,formated_data):
#     prompt = f"""  

#     Answer the question using below data

#     News : 
#     {formated_data}

#     Question : {query}
#     """
#     return prompt

# def llm_call(prompt):
#     output = client.chat.completions.create(
#         model="deepseek-chat",
#         messages=[
#             {'role':'user','content':prompt}
#         ]
#     )
#     return output.choices[0].message.content

# query = "tell me about maheswar reddy"
# data = news_relevant_data(query)
# formated = news_format(data)
# prompt = genrate_final_prompt(query,formated)
# answer = llm_call(prompt)
# print(answer)



correct = [0]
relevant = retrieve('tell claude 4',5)

relevant_count = 0
for index in relevant:
    if index in correct:
        relevant_count+=1
k = len(relevant)

def precision_at_k(relevant_count, k):
   return relevant_count/k

print(precision_at_k(relevant_count,k))


def recall_at_k(relevant_count , total_relevant):
    return relevant_count/total_relevant

count = len(correct)
print(recall_at_k(relevant_count,count))
    