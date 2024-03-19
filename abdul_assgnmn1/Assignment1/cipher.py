import math

def substitutionEncrypt(text, key):
    cipher = ""
    for char in text: # Every char datatype in the text
        # Shift it
        pos = (ord(char) + key) % 255
        cipher += chr(pos) # Get the new char
    return cipher

def substitutionDecipher(cipherText, key):
    text = ""
    for char in cipherText: # catch every char in cipherText
        # Value of oroginal character minus the key modulo 255.
        pos = (ord(char) - key) % 255
        text += chr(pos) # Regain the original character
    return text

# Function that removes duplicate letters in a string,
# since the column cipher cannot handle duplicate letters.
def remove_duplicates(key):
    seen = set()
    return ''.join(char for char in key if char not in seen and not seen.add(char))

def columnCipher(text, key1):
    cipher = ""
    key = remove_duplicates(key1)
    # Converting the file to a list so we can cipher it.
    textList = list(text)
    sortedKey = sorted(key) # get the index from key
    col = len(key)  # get the number of columns
    textLenght = len(text)
    row = int(math.ceil(textLenght / col)) # Number of rows we're gonna need.
    
    filler = int((row * col) - textLenght) # Fill empty boxes with a filler character.
    textList.extend("%" * filler)

    messageBox = [textList[i: i + col] for i in range(0, len(textList), col)] 

    # Use the message box to encrypt message.
    i = 0 
    for pointer in range(col):
        Index = key.index(sortedKey[i])
        for row in messageBox:
            cipher += row[Index]
        i += 1
    return cipher


def columnDecipher(cipher, key1):
    text = ""
    cipherList = list(cipher)
    key = remove_duplicates(key1)

    sortedKey = sorted(key) # get the index from key.
    # Get the number of rows and columns we're gonna need.
    col = len(key)
    cipherLengt = len(cipher) 
    row = int(math.ceil(cipherLengt / col))
    
    emptyMessageBox = [[None] * col for i in range(0, cipherLengt, col)]

    listIndex = 0
    try:
        for i in range(col):
            #This will give us the index of our cipher, we have to place them backwards.
            cipherIndex = key.index(sortedKey[i])

            for j in range(row):
                # This will go progressively down the rows and columns and rearrange our original text.
                # Still need to fetch the letters later on.
                emptyMessageBox[j][cipherIndex] = cipherList[listIndex]
                listIndex += 1
    # Error handling. IndexErrors are weird.             
    except IndexError:
        raise IndexError("Key dosent not fit the given cipher")
    try:
        # Now that the box is correctly filled, we need to fetch the letters in the right sequence.
        for i in range(row):
            for j in range(col):
                if emptyMessageBox[i][j] is not None:
                    text += emptyMessageBox[i][j]
    except TypeError:
        raise TypeError("This program, can't handle key with repeating letters")

    return text.rstrip("%")  


# Read file, retrieves the text inside of file

def readFile(file):
    with open(file, "r", encoding="utf8") as the_file:
        data = the_file.read()
    return data

# Write file, overwrites data in a file with new data.

def writeFile(file, content):
    with open(file, "w", encoding="utf8") as file:
        for char in content:
            file.write(char)


# Main method
while True:
    choice = int(input("""
    Please pick an Encryption.
    1- Substitution 
    2- Transpostion
    3- Exit
    """))

    if choice == 1:

        while True:

            menuOne = int(input("""
            1- Cipher
            2- Decipher
            3- Go back
            """))

            # Substitiution encrypt and decrypt.
            if menuOne == 1: 
                file = input("""
                Enter the name of the file you want to cipher.
                """)
                key = int(input("Enter a key between 1-255: "))
                cipher = substitutionEncrypt(readFile(file), key)
                newFile = input("""
                Enter the name of a new file or overwrite the current file.
                """)
                writeFile(newFile, cipher)

            if menuOne == 2:
                file = input("""
                Enter the name of the file you wnat to decipher.
                """)
                key = int(input("Enter a shift key between 1-255: "))
                text = substitutionDecipher(readFile(file), key)
                newFile = input("""
                Enter the name of a new file or overwrite the current file.
                """)
                writeFile(newFile, text)

            if menuOne == 3:
                print("Rolling back \n")
                break
    

    # Transpostion cipher and decipher
    if choice == 2: 
        menuTwo = int(input("""
            1- Cipher
            2- Decipher
            3- Go back
            """))
        if menuTwo == 1:
            file = input("""
            Enter the name of the file you want to cipher.
            """)

            print("With this type of cipher, the key is a word!")
            key = input("Enter The key: ").lower()
            cipher = columnCipher(readFile(file), key)
            newFile = input("""
            Enter the name of a new file or file you want to overwrite.
            """)
            writeFile(newFile, cipher)

        if menuTwo == 2: 
            file = input("""
            Enter the name of the file
            """)

            key = input("Enter The key: ").lower()
            text = columnDecipher(readFile(file), key)
            newFile = input("""
            Enter the name of a new file or file you want to overwrite.
            """)
            writeFile(newFile, text)
        
        if menuTwo == 3: # Break check statment
            print("Rolling back \n")
            break

    if choice == 3:
        print("Later biiiiiiiii-.")
        break