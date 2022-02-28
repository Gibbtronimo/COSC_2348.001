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


if __name__ == "__main__":
    print("Problem 1:\n")
    morseCode()

    print("\nProblem 2:\n")
    strAnalysis = input("Enter a string: ")
    vnum = strVowels(strAnalysis)
    cnum = strConsts(strAnalysis)
    print("There are",vnum,"vowels")
    print("There are",cnum,"consonants")
