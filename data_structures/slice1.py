name = "Anushka Saxena"
firstname = name[:8]
print(firstname)
lastname = name[8:]
print(lastname)
even_index = name[::2]
print(even_index)
odd_index = name[1::2]
print(odd_index)

#reversing a sequence with slicing 
reversed_name = name[::-1]
print(reversed_name)
print(name[:]) #won't effect
print(name[::-1][:7][::-1]) #runs sequentially
print(name[3:-3])
