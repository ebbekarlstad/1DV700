def transposition_cipher(text, key, mode):
    def build_matrix(text, nrows, ncols):
        # Build the matrix with placeholders for the encryption.
        matrix = []
        for _ in range(nrows):
            # Create a new row with empty strings for each column
            row = []
            for _ in range(ncols):
                row.append('')
            matrix.append(row)

        idx, jdx = 0, 0
        for char in text:
            # Consider only alphabetic characters for transposition
            if char.isalpha():
                matrix[idx][jdx] = char
                jdx += 1
                if jdx == ncols:
                    jdx = 0
                    idx += 1
        return matrix

    def encrypt(matrix, text, nrows, ncols):
        # Read the matrix in a column-wise fashion to get the encrypted text.
        result = []
        for j in range(ncols):
            for i in range(nrows):
                if matrix[i][j] != '':
                    result.append(matrix[i][j])
        # Re-insert non-alphabetic characters at their original positions
        idx_alpha = iter(result)
        encrypted_text = []
        for char in text:
            if char.isalpha():
                encrypted_text.append(next(idx_alpha))
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)

    def decrypt(matrix, text, nrows, ncols):
        # Extract alphabetic characters from the ciphertext
        ciphertext_alpha = []
        for char in text:
            if char.isalpha():
                ciphertext_alpha.append(char)

        idx_alpha = iter(ciphertext_alpha)
        # Fill the matrix with the extracted alphabetic characters
        for j in range(ncols):
            for i in range(nrows):
                if matrix[i][j] != '':
                    matrix[i][j] = next(idx_alpha)
        # Reconstruct the plaintext with non-alphabetic characters
        result = []
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] != '':
                    result.append(matrix[i][j])
        idx_alpha = iter(result)
        decrypted_text = []
        for char in text:
            if char.isalpha():
                decrypted_text.append(next(idx_alpha))
            else:
                decrypted_text.append(char)
        return ''.join(decrypted_text)

    # Calculate the number of rows and columns for the matrix
    nrows = key
    alpha_chars = []
    for char in text:
        if char.isalpha():
            alpha_chars.append(char)
    ncols = len(alpha_chars) // nrows
    if len(alpha_chars) % nrows != 0:
        ncols += 1

    if mode == 'e':  # Encryption
        matrix = build_matrix(text, nrows, ncols)
        return encrypt(matrix, text, nrows, ncols)
    elif mode == 'd':  # Decryption
        # For decryption, the matrix is initially filled with
        # placeholders for alphabetic characters
        placeholder_text = 'A' * len(alpha_chars)
        matrix = build_matrix(placeholder_text, nrows, ncols)
        return decrypt(matrix, text, nrows, ncols)
