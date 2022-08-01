amt = int(input('How much kg of apples you want'))
if amt >5:
    price = 80
    total = amt * price
else :
    price =90
total = amt * price
print (f'You have to pay Rs{total} for {amt} kg. of apples')