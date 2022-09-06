a = [1,2,3,3,1,2,2,3,3,3,1,1,1,1,2,2,2,2,3,3,3,1,1,1]

clean_a = list (filter(lambda i : i!=1,a))
print (clean_a)

files = ['a.png', 'b.jpg', 'c.jpg', 'd.png']
jpeg  = list (filter(lambda i : i.endswith('.jpg'),files))
png = list (filter(lambda i : i.endswith('.png'),files))

print (jpeg)
print (png)