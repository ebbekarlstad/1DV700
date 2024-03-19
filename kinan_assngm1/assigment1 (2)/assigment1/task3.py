from math import ceil
import os

# Alphabet for substitution cipher
Alphabet = [chr(i) for i in range(256)]

# substituation cipher's function
def substitution(text, encrypt, key):
    new_text = ""
    for char in text:
        if char in Alphabet:  # Check if the character is in the Alphabet
            index = Alphabet.index(char)
            if encrypt:
                new_index = (index + key) % 256
            else:
                new_index = (index - key) % 256
            new_text += Alphabet[new_index]
        else:
            new_text += char  # Keep the character as it is if not in Alphabet
    return new_text

#a function for transposition's encrypt
def transposition_encrypt(key, msg):
    ciphertext = [""] * key
    for c in range(key):
        currindex = c

        while currindex < len(msg):
            ciphertext[c] += msg[currindex]
            currindex += key
    return "".join(ciphertext)

#transposition cipher's decrypt function
def transposition_decrypt(key, msg):
    number_columns = int(ceil(len(msg) / float(key)))
    number_rows = key
    number_shaded = (number_columns * number_rows) - len(msg)

    table = [""] * number_columns
    column = 0
    row = 0

    for letter in msg:
        table[column] += letter
        column += 1

        if (column == number_columns) or (column == number_columns - 1 and row >= number_rows - number_shaded):
            column = 0
            row += 1
    return "".join(table)

#this function is to handle the user inputs 
def file_process(method, user_choice, file_name, key):
    text = [] #list to add each new (decrypted or encrypterd) line  
    encrypt = user_choice == 'e'
    file_path = os.getcwd()
    file_path += "\\" + file_name + ".txt"

    with open(file_path, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            if method == 's':
                text.append(substitution(line, encrypt, key))
            elif method == 't':
                if encrypt:
                    text.append(transposition_encrypt(key, line))
                else:
                    text.append(transposition_decrypt(key, line))

    output_file_path = file_path.replace(".txt", "_encrypted.txt") if encrypt else file_path.replace(".txt", "_decrypted.txt")

    with open(output_file_path, 'w') as file:
        for line in text: 
            file.write(line + "\n")

def main():
    method = input("Enter 's' for substitution, 't' for transposition: ")
    user_choice = input("Enter 'e' to encrypt, 'd' to decrypt: ")
    file_name = input("Enter the file name: ")
    key = int(input("Enter a key for encryption/decryption: "))
    
    file_process(method, user_choice, file_name, key)

main()
