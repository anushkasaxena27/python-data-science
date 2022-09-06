#anonymous function without name
f = lambda x: x + x**2  #lambda expression

print (f)
ans = f(5)
print (ans)

for i in range (1,10):
    print(f(i))

g = lambda a,b: (a+b)*(b+a)+1
print (g(2,3))
print(g(2,2))
print(g(44,50))
print (g(2,12))
