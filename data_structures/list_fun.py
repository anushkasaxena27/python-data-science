fruits = []
print(fruits)
fruits.append('apple')
fruits.append('banana')
fruits.append('orange')
fruits.append('mango')
print(fruits)
#insert at specified position
fruits.insert(2,'kiwi')
print(fruits)

dry_fruits = ['Almonds','Cashew','Walnut','Dates','Raisins']
#to merge two list
fruits.extend(dry_fruits)   #adds to fruits
print(fruits)

#Sort function
fruits.sort()
print(fruits)

#Remove function
fruits.remove('apple')
print(fruits)

#fruits.remove('Cherry')
#print(fruits)

#reverse

fruits.sort(reverse = True)
print(fruits)

