import os


path = '\\Downloads\\'

print('Is path OK?')

if os.path.exists(path) == True:
    print(True)

else:
    print(False)

print('Testing github verification')