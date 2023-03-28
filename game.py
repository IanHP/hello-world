"""
This is a super awesome little game!!!!!
"""

def setVars(wordList):
    '''
    puts data from a list of lists (where [i][0] = name and [i][2] = value, and each [i] is a new key:value) into dictionary
    '''

    variables = {}

    for index,line in enumerate(wordList):
        '''
        runs as each list in the list of lists
        '''

        #checks if list is formatted properly. If yes returns the key and value.
        check,key,value = checkLineForKeyValue(index,line)

        #checks if key is already in use
        keyList = variables.keys()

        if key in keyList:
            check = False
            print(f'Duplicate key on line {index}')


        if check:
            #then turns value into correct form.
            value = stringToValue(value)

            #adds key:value to dictionary
            variables[key] = value


    return variables

def checkLineForKeyValue(index,line):
    '''
    checks if the line has the correct syntax. Then returns edited list.
    '''

    length = len(line) 
    if length >= 2 and line[1] == '=':
        return True,line[0],line[2]
    else:
        print(f'Improperly formatted key:value pair on line {index}')
        return False,"error","error"
    


def stringToValue(value):
    '''
    Transforms a string into a:
    1. integer, 2. float, 3. list
    else: does nothing
    '''

    if value.isdigit():
        return int(value)
    elif is_float(value):
        return float(value)
    elif is_list(value):
        return listify(value)
    else:
        return value


def is_float(word):
    '''
    Checks if the string is a float
    '''
    try:
        float(word)
        return True
    except ValueError:
        return False

def is_list(word):
    '''
    Checks if the string is a list
    '''
    return word[0] == "[" and word[-1] == "]"

def listify(word):
    '''
    Turns a string into a list
    '''
    word = word[1:len(word)-1]

    word = word.split(",")
    newList = []
    for part in word:
        newList.append(stringToValue(part))
    return newList


if __name__  == "__main__":
    '''
    if run it will turn the inputted file into a dictionary of key:values.
    Supported Values:
     - Integers
     - Floats
     - Lists
     - All othres will become strings
    
    '''
    #gets user input for file name
    print('What is the file named? If it is not in the same folder, please include the necessary directory info. \nenter here: ')
    fileLocation = input()

    #sets the file to variable
    file = open(fileLocation,mode='r')
    text = file.read()
    file.close()

    #turns text into list based on each line
    lineList = text.split('\n')

    #turns text into list of lists. Line is 1st Dim. Each word is 2nd Dim.
    wordList = []
    for line in lineList:
        wordList.append(line.split(' '))

    #Creates the dictionary.
    values = setVars(wordList)
    print(values)







