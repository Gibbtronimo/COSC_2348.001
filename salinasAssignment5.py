'''
    Assignment 5
    Ryan Salinas
    2/28/22
'''
# Problem 1: More Code String Converter
#            - a morse code dictionary is used to convert a user-input string into morse code

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
    userString = userString.lower()
    for ch in userString:
        print(morseTable[ch],end='')

# Problem 2: String Analysis
#            - these functions count the number of vowels and consonants in a user-input string

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

# Problem 3: String cleanup
#            - these programs will apply string functions to the strings inputted

# Function 1 for Problem 3
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
def part2(string):
    newstr = ""
    for ch in string:
        if ch.isalpha() or ch.isspace():
            newstr += ch
    return newstr

# Function 3 for Problem 3
def part3(string):
    newstr = ""
    for ch in string:
        if ch.isalpha():
            newstr += ch
        else:
            newstr += ' '
    return newstr

# Function 4 for Problem 3
def part4(string):
    newstr = ""
    for ch in string:
        if ch not in vList:
            newstr += ch
    return newstr

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

