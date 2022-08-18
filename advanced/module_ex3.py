import os

print('Current Folder')
print(os.getcwd())
print(os.listdir())

print ("C Drive Content")
os.chdir('C:\\Program Files')
print(os.getcwd())
print(os.listdir())

address = r'C:\Program Files\Python\python.exe'
#address = r'C:\Users\saxen\OneDrive\Desktop\anushka\python\string2.py'
if os.path.exists(address):
    print('File Exists')
else:
    print('File does not exist')