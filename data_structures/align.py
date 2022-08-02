word = 'python'

#left align
print(word.ljust(80))
#right align
print(word.rjust(80))
#center align
print(word.center(80))

#fillchar examples
#left align
print(word.ljust(80,'-'))
#right align
print(word.rjust(80,'#'))
#center align
print(word.center(80,'^'))

#printing a formatted table 0f 3
print('-'*40)
for i in range(1,11):
    r =3*i
    print(3,'x',str(i).rjust(2),'=',r)