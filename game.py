"""
This is a super awesome little game!!!!!
"""



file = open('test.txt',mode='w+')


file.write("hello")
print(file.read())
file.close()