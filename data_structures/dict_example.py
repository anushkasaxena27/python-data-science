my_dict = {'name': 'Jack','age':22}
print(my_dict)
print(my_dict['name'])
print(my_dict.get('age'))  #better to use get than []
#Trying to access that does not exist -- throws error
#print(my_dict['address'])
print(my_dict.get('address')) #does not throw error 

#MODIFYING ELEMENTS
#update value
my_dict['age'] = 27
print(my_dict)
#add item
my_dict['address'] = 'Downtown'
print (my_dict)

#REMOVING ELEMENTS
SQUARES = {1:1,2:4,3:9,4:16,5:25}
print(SQUARES.pop(4))  #remove particular item, returns value
print(SQUARES.popitem()) #remove last element ,return (key,value)
SQUARES.clear() #remove all items
del SQUARES #delete dictionary itself

#TRAVERSING
squares = {1:1,2:4,3:9,4:16,5:25}
for i in squares:  #only keys
    print(i)
for i in squares:
    print(squares[i])  #only values
for k,v in squares.items():  #both key and values
    print(k,v)
