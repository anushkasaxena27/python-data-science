x = [1,2,3,3,5,1,2,3,1,2]
#x2 = [ i**2 for i in x ]   # list comprehension
x2 = map(lambda i : i**2,x)

x3 = tuple (map (lambda i : (i,i**3),x))# tuple with x cubes
# for i in x2:
#     print (i)

print (list(x2))
print (x3) 

y = ['apple','banana','orange','mango','grapes']
z = ['pie','shake','icecream','pudding','pastry','jam']

words = set (map (lambda a,b : a +'-'+b,y,z))
print (words)

#single line input with multiple
numbers = list (map(int,input ('enter 10 number :').split()))
print (numbers)
