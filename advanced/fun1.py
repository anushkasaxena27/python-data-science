# def fun_name(]parameters]):
#    statements
#    [return expression]

#defining
def hello():
    print('👋 Hello!')
    print('world 🌍')

#calling or using
hello()
hello()

def greetings(message):
    print('👋',message)

greetings('world')
greetings('hola amigos')
greetings('bonjour amis')
greetings('Namaste Dosto')

def calc_area(w,h):
    area = w*h
    print('area:  ', area)
# passing values to function
calc_area(10,20)
calc_area(3,5)
calc_area(100,200)


def calc_area_v2(w,h):
    area = w*h
    return area
#display
print(calc_area_v2(10,20))
print(calc_area_v2(3,5))

#storing return value in a variable
ans = calc_area_v2(10,20)
print (ans)

#using return values in a expression
ans = calc_area_v2(3,5)+ calc_area_v2(10,20)
print(ans)