A = {1,2,2,3,4,5,6,10}
#Set Union
B = {4,5,5,6,2,7,8,11,16}
print(A|B)   #using | operator
print(A.union(B))    #using union function
print(B|A)

#Set Intersection
print(A&B)
print(A.intersection(B))

#Set Difference
print(A-B)
print(A.difference(B))
print(B-A)

#Symmetric Difference 
print(A^B)
print(A.symmetric_difference(B))

#Subset
x = {2,3,4,5,6}
y = {2,3,4,5,6,1,8,9,7}
print(x.issubset(y))
z = {3,5,8,10,11}
print(x.issubset(z))
a = {12,13,14}
print(a.isdisjoint(y))
print(y.issuperset(x))

#List -> Set -> List
x = [2,2,3,5,5,6,6]
xs = set(x)
xl = list(set(x))
print(x)
print(xs)
print(xl)
