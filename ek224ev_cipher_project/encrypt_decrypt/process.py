from substitution import substitution_cipher
from transposition import transposition_cipher


# Function to process the file
def process_file(file_path, method, key, mode):
    try:
        # Open and read file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        if method == '1':
            # Use Substitution Cipher
            result = substitution_cipher(content, key, mode)
        elif method == '2':
            # Use Transposition Cipher
            # Convert key to integer for transposition cipher
            key = int(key) if method == '2' else key
            result = transposition_cipher(content, key, mode)

        # Determine the output file name based on the mode
        if mode == 'e':
            output_file_name = "encrypted.txt"
        else:
            output_file_name = "decrypted.txt"

        # Write result to the output file
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.write(result)

        print(f"\nProcess completed. Result written to {output_file_name}\n")

    except FileNotFoundError:
        print(f"\nFile not found: {file_path}\n")
