def substitution_cipher(text, key, mode):
    result = ""

    # Convert the key to an integer and ensure it's
    # within the 8-bit range (0-255)
    key = int(key) % 256
    if mode == 'd':  # 'd' for decrypt; negates the key
        key = -key

    # Iterate over each character in the text
    for char in text:
        # Check if the character is an asterisk, space, newline,
        # carriage return, or tab and leave it unchanged
        if char in ('*', ' ', '\n', '\r', '\t'):
            result += char
            continue

        # Convert character to its ASCII code
        char_code = ord(char)

        # Shift character by key positions and wrap within the 8-bit range
        new_code = (char_code + key) % 256

        # Append the shifted character to the result
        result += chr(new_code)

    return result
