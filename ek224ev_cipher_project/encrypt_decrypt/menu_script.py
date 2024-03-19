from process import process_file

print('\033[1m' + '\nWelcome to the Encryption/Decryption program!')
print('\033[0m')

print("Choose an encryption method:")
print("1: Substitution Cipher")
print("2: Transposition Cipher")

method = input("Method (1 or 2): ")

print("\nChoose the mode:")
print("'e': Encryption")
print("'d': Decryption")

mode = input("Mode ('e' or 'd'): ")

key = input("\nEnter your key [0 - 255]: ")

if mode == 'e':
    file_action = "encrypt"
else:
    file_action = "decrypt"

plain_file = input(f"\nEnter the name of the file you want to {file_action}: ")

# Assuming the output file name is based on the mode
if mode == 'e':
    cipher_file = "encrypted.txt"
else:
    cipher_file = "decrypted.txt"

# Call the process_file function with user inputs
process_file(plain_file, method, key, mode)
