val = int(input('Enter a number'))
if val >100:
    val /=2
else:
    val *=2
print('>>The result is:',val)

# true situation if condition else false situation
val = val/2 if val > 100 else val *2
print(f'>>The result is: {val}') 


name = input("Enter ur name")
if name.isalpha():
    print ("very good")
else:
    print ("not good")
#oneliner
print("very good") if name.isalpha() else print ('not good')

