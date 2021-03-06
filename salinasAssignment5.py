'''
    Assignment 5
    Ryan Salinas
    2/28/22
'''
import statistics # Problem 4
import re # Problem 5

#-------------------------------------------------------------------------------------------------
# Problem 1: More Code String Converter
#            - a morse code dictionary is used to convert a user-input string into morse code
#-------------------------------------------------------------------------------------------------

# Morse Code Dictionary for problem 1
morseTable = {' ':' ',',':'--..--','.':'.-.-.-','?':'..--..',
              '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
              '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
              'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.',
              'g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..',
              'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.',
              's':'...','t':'-','u':'..-','v':'...-','x':'-..-','y':'-.-','z':'--..'}
def morseCode():
    print("Allowable characters: ' ,.?', 0-9, a-z")
    userString = input("Enter a string to convert to morsecode: ")
    try:
        userString = userString.lower()
        for ch in userString:
            print(morseTable[ch],end='')
    except:
        print("You entered a character that was not allowed!")

#------------------------------------------------------------------------------------------------
# Problem 2: String Analysis
#            - these functions count the number of vowels and consonants in a user-input string
#------------------------------------------------------------------------------------------------

# Vowel list used in both functions
vList = ['a','e','i','o','u']

# Function to count vowels
def strVowels(strInput):
    strInput = strInput.lower()
    vowels = 0
    for ch in strInput:
        if ch in vList:
            vowels += 1
    return vowels

# Function to count consonants
def strConsts(strInput):
    strInput = strInput.lower()
    consts = 0
    for ch in strInput:
        if (ch not in vList) and ch.isalpha():
            consts += 1
    return consts

#-----------------------------------------------------------------------------------------------
# Problem 3: String cleanup
#            - these programs will apply string functions to the strings inputted
#-----------------------------------------------------------------------------------------------

# Function 1 for Problem 3
# - counts digits and symbols in the string
def part1(string):
    letters = 0
    digits = 0
    symbols = 0
    for ch in string:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1
        else:
            symbols += 1
    print("String 1: ",string)
    print("Letters: ",letters)
    print("Digits: ",digits)
    print("Symbols: ",symbols)

# Function 2 for Problem 3
# - removes special symbols and punctuation
def part2(string):
    newstr = ""
    for ch in string:
        if ch.isalpha() or ch.isspace():
            newstr += ch
    return newstr

# Function 3 for Problem 3
# - removes '-' and replaces with ' '
def part3(string):
    newstr = ""
    for ch in string:
        if ch.isalpha():
            newstr += ch
        else:
            newstr += ' '
    return newstr

# Function 4 for Problem 3
# - removes all consonants
def part4(string):
    newstr = ""
    for ch in string:
        if ch not in vList:
            newstr += ch
    return newstr

#----------------------------------------------------------------------------------------------
# Problem 4: Exception handling
#            - create list, find average/median/standard deviation, and create new list
#            - with division of first and second elements as new elements
#----------------------------------------------------------------------------------------------

# Function 1 for Problem 4
def makeList(uList):
    try:
        print("Enter 'n' number of inputs for the list (n>10)")
        print("The values must be between 0 to 100 inclusive")
        n = int(input("List size: "))
        total = 0
        if n > 10:
            for i in range(0,n):
                num = int(input("Enter a number: "))
                if (num >= 0) and (num < 100):
                    uList.append(num)
                    total += num
                else:
                    print("The number needs to be at least 0 and at most 100")
        else:
            print("The list size must at least be 10")

        average = total/len(uList)
        print("Average: ",round(average,3))
        median = statistics.median(uList)
        print("Median: ",round(median,3))
        std_dev = statistics.stdev(uList)
        print("Standard Deviation: ",round(std_dev,3))

    except:
        print("Input must be an integer") 

# Function 2 for Problem 4
def newList(uList):
    newList = []
    for i in range(0,len(uList)-1):
        try:
            num = uList[i]/uList[i+1]
            newList.append(round(num,2))
        except ZeroDivisionError:
            print("Cannot divide by zero!\n")
    return newList

#---------------------------------------------------------------------------------------------
# Problem 5: String Conversion Using Loops
#            - Convert a given string to different variations
#---------------------------------------------------------------------------------------------

# Function 1 for Problem 5
# - makes the first letter of each word in the string uppercase
def upperCase(string):
    newstring = ""
    split = re.split('\s',string)
    for w in split:
        newstring += w[0].upper()
        newstring += w[1:len(w)].lower() + ' '
    return newstring

# Function 2 for Problem 5
# - removes the spaces from the string
def noSpaces(string):
    newstring = ""
    string = upperCase(string)
    split = re.split('\s',string)
    for w in split:
        newstring += w
    return newstring


# Function 3 for Problem 5
# - replaces all instances of 's' with '$' and removes the first 'the' in the string
def sToCash(string):
    newstring = ""
    string = upperCase(string)
    split = re.split('[sS]',string)
    split = split[:len(split)-1]
    for w in split:
        newstring += w + '$'
    split2 = re.split('\s',newstring)
    del split2[2]
    newstring = ""
    for w in split2:
        newstring += w + ' '
    return newstring


# Function 4 for Problem 5
# - only applies upper case to the non-article words (nouns?)
def selectUpper(string):
    newstring = ""
    split = re.split('\s',string)
    for w in split:
        if w == split[0] or w == split[3] or w == split[6]:
            newstring += w[0].upper()
            newstring += w[1:len(w)] + ' '
        else:
            newstring += w + ' '
    return newstring

# Main function
if __name__ == "__main__":
    print("Problem 1:\n")
    morseCode()

    print("\n\nProblem 2:\n")
    strAnalysis = input("Enter a string: ")
    vnum = strVowels(strAnalysis)
    cnum = strConsts(strAnalysis)
    print("There are",vnum,"vowels")
    print("There are",cnum,"consonants")

    print("\nProblem 3:\n")
    str1 = "P@#yn26at^&i5ve"
    part1(str1)

    # Output shows changed string through function for str2,str3,str4
    str2 = "/*Jon is @developer & musician"
    print("\nString 2 before: ",str2)
    str2 = part2(str2)
    print("String 2 after: ",str2)

    str3 = "Emma-is-a-data-scientist"
    print("\nString 3 before: ",str3)
    str3 = part3(str3)
    print("String 3 after: ",str3)

    str4 = "Hello,have a good day"
    print("\nString 4 before: ",str4)
    str4 = part4(str4)
    print("String 4 after: ",str4)

    print("\nProblem 4:\n")
    userList = []
    makeList(userList)
    print("User list: ",userList)
    userList = newList(userList)
    print("New list: ",userList)

    print("\nProblem 5:\n")
    str5 = "this is the string for the class"
    print("String 5: " + str5)
    print("1: " + upperCase(str5))
    print("2: " + noSpaces(str5))
    print("3: " + sToCash(str5))
    print("4: " + selectUpper(str5))
