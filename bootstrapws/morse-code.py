"""
Kody Summers 
CSCI 135
Module 7 Problem 2
Morse Code Interpreter
"""


# Creates a dictionary of letters didgits and morse code
def getMorseCode():
    morseCode = {
        "A": ".-",    "B": "-...",  "C": "-.-.",
        "D": "-..",   "E": ".",     "F": "..-.",
        "G": "--.",   "H": "....",  "I": "..",
        "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",
        "P": ".--.",  "Q": "--.-",  "R": ".-.",
        "S": "...",   "T": "-",     "U": "..-",
        "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..",
        "9": "----."
    }

    return morseCode


#Gets user input for what translation they want and validates the input
def getTranslationChoice():
    while True:
        choice = input("Translate English to morse code (E) or from Morse code to English (D)? ").upper().strip()
        if choice in ["E", "D"]:
            return choice
        else:
            print("Invalid choice. Please enter 'E' for english to morse code or 'D' for morse code to english.")


#Gets user input for english message and validates the input
def getEnglishInput(morseCode):
    while True:
        message = input("Enter a message using letters, didgits , and spaces:").upper().strip()

        if message == "":
            print("Message cannot be empty. ")
            continue 

        valid = True

        for char in message:
            if char not in morseCode and char != " ":
                valid = False
                break

        if valid:
            return message
        else:
            print("Please use only letters, didgits, and spaces.")


#Encodes the message into morse code
def encodeMessage(message, morseCode):
    encodedMessage = []

    for word in message.split():
        encodedLetters = []

        for char in word:
            encodedLetters.append(morseCode[char])

        encodedMessage.append((" " * 3).join(encodedLetters))

    return (" " * 7).join(encodedMessage)


#Decodes the morse code message into english
def decodeMessage(message, morseCode):
    
    englishCode = {}

    for letter, code in morseCode.items():
        englishCode[code] = letter

    decodedWords = []

    for word in message.split(" " * 7):
        decodedLetters = []

        for code in word.split(" " * 3):
            decodedLetters.append(englishCode[code])

        decodedWords.append("".join(decodedLetters))

    return " ".join(decodedWords)


#Gets user input for morse code message and validates the input
def getMorseInput(morseCode):
    print("Use dots and dashes, with 3 spaces between letters")
    print("and 7 spaces between words.")

    while True:
        message = input("Enter your Morse code: ").strip()

        if message == "":
            print("Message cannot be empty.")
            continue

        valid = True

        for word in message.split(" " * 7):
            for code in word.split(" " * 3):
                if code not in morseCode.values():
                    valid = False
                    break

            if not valid:
                break

        if valid:
            return message
        else:
            print("Invalid Morse code or spacing. Please try again.")


#Main function to run the Morse Code Interpreter
def main():
    print("Welcome to the Morse Code Interpreter!")

    morseCode = getMorseCode()
    choice = getTranslationChoice()

    if choice == "E":
        message = getEnglishInput(morseCode)
        result = encodeMessage(message, morseCode)
    else:
        message = getMorseInput(morseCode)
        result = decodeMessage(message, morseCode)

    print("Translated message:", result)



#Calls the main function 
main()