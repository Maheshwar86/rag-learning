#now we going to lists in this lists is ordered , changeable , and allow duplicates also 
l1 = ['Mahesh','Siva','Hemanth','Sai','Chakri','Mani','Humans']
print(f"this is list : {l1}")

# now adding item in that list
l1.append('Devil')
print(f"after adding 'devil' word {l1}")

#now removing item
l1.remove('Devil')
print(l1)

# this list not return any value adding time and removing time 
#here for test

result = l1.append('this is test')
print(result)