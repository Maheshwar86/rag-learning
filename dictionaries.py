Person={
    'name':'Mahesh',
    'age':110,
    'place':'Earth'
}
print(Person)


#now accessing a value

print(Person['name'])
print(Person['place'])


# Now Adding New Keys+Values

Person['mail'] = 'Alien@gmail.com'
print(Person)


#now items method ok (.items())
for key , value in Person.items():
    print(f"Key : {key}    value : {value}")

