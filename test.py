from openai import OpenAI

dtao = OpenAI(
    api_key="sk-0f12cd4e6043463fa9b39f06d262d04c",
    base_url="https://api.deepseek.com/"
)

ans = dtao.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {'role':'user' , 'content':'tell me about humans in one line'}
    ]
)

#print(f"Role : {ans.choices[0].message.role}")
#print(f"Content : {ans.choices[0].message.content}")
print(f"full info : {ans}")