person = [
    {'name':'Mahesh','Age':24 , 'Place':'Earth','mail':'Alien@gmail.com'},
    {'name':'Hemanth','Age':25 , 'Place':'Earth','mail':'Hemanth@gmail.com'}
]


t = []
for x in person:
    str = f"Name : {x['name']} Age : {x['Age']}"
    t.append(str)
format_str = "\n" .join(t)
print(format_str)