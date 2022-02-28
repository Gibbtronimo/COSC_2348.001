'''
    Assignment 5
    Ryan Salinas
    2/28/22
'''
# Problem 1: More Code String Converter
#            - a morse code dictionary is used to convert a user-input string into morse code

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

if __name__ == "__main__":
    print("Problem 1:\n")
    morseCode()
