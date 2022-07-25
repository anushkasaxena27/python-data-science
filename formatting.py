product = input("What item did you buy?")
price = float(input("How much did you pay"))
qty = int(input("how many did you buy?"))

print("You purchased",qty,product,'for',price)
#formatted string
print (f'You purchased {qty}{product} for {price}')