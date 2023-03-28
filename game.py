"""
This is a super awesome little game!!!!!
"""



file = open('test.txt',mode='w')
file.write("")
file.close()

file = open('test.txt',mode='a')
for i in range(0,3):
    file.write(f"{i}: hello!\n")
file.close()

file = open('test.txt',mode='r')
print(file.read())
file.close()