#COMPREHENSIONS
#-used when we want to create a new list by performing some operations on existing list
#---------SYNTAX-------------
#newlist = [expression for loop conditon*optional*]

x = [12,5,64,5,34,2,3]
x2 = [ i**2 for i in x]
print (x2)

y = [2,3,5,6,7,7,2]
z= [ i+j for i,j in zip(x,y)]  #zip is used to run x,y together in a single loop
print (z)