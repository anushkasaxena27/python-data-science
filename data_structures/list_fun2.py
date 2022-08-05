#Count function
x = [1,1,2,1,1,1,2,3,1,2,1,1,3,3,2,5,5,5,5,6,6,6,6,2,1]
print("Total no. of 1 = " ,x.count(1))
print("Total no. of 2 = " ,x.count(2))
print("Total no. of 3 = " ,x.count(3))
print("Total no. of 5 = " ,x.count(5))
print("Total no. of 6 = " ,x.count(6))

movies = ['Batman', 'DDLJ' , 'Krishh', 'Avengers','Dr.Strange', '3 Idiots','ZNMD','KGF','RRR']
print(movies.index('Dr.Strange'))
#print(movies.index('Harry Potter'))   ValueError: 'Harry Potter' is not in list

#Copy Function
blockbusters = movies.copy()
print("Duplicated List = ",blockbusters)

#CLear Function
blockbusters.clear()
print(blockbusters)

#POP function

print("After popping = ",movies.pop())
print("After popping 4 index = ",movies.pop(4))
print("After popping 6 index = ",movies.pop(6))
#print('Popping unavailable index = ',movies.pop(11))         IndexError: pop index out of range
print(movies)