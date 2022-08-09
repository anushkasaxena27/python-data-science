names = ['Bruce Wayne', 'Clark Kent','Wally West']
# initials =[]
# for name in names:
#     parts = name.split()
#     initials.append(parts[0][0]+parts[-1][0])

initials = [name.split()[0][0]+'.'+ name.split()[-1][0]+'.' for name in names]
print (initials)