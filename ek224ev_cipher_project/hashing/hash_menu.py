import matplotlib.pyplot as plt

# Nice Welcome screen
print('\033[1m' + '\nWelcome to the Hash Function Program!')
print('\033[0m')


def hash_function(input_string):
    # Calculate the sum of ASCII values
    # of all the characters in the input string
    ascii_sum = sum(ord(char) for char in input_string)
    # Use modulo operation to confine the range of the hash to 0-255 (8 bits)
    return ascii_sum % 256


def bit_difference(hash1, hash2):
    # XOR the two hashes to determine which bits are different
    xor_result = hash1 ^ hash2
    # Count and return the number of bits that are set to 1 in the XOR result
    return bin(xor_result).count("1")


def avalanche_test(words):
    previous_hash = None
    differences = []

    for word in words:
        # Compute the hash value of the current word
        current_hash = hash_function(word)
        # If it's not the first word, calculate the bit
        # difference from the previous hash
        if previous_hash is not None:
            difference = bit_difference(previous_hash, current_hash)
            differences.append(difference)  # Add the difference to the list
        # Update previous_hash for the next iteration
        previous_hash = current_hash

    return differences


def uniformity_test(words):
    # Initialize a dictionary to count the frequency of each hash value
    frequency = {i: 0 for i in range(256)}

    for word in words:
        # Compute the hash value of the current word
        hash_value = hash_function(word)
        # Increment the frequency count for this hash value
        frequency[hash_value] += 1

    return frequency


def readFile(file):
    # Open, read, and split a file (by line-break)
    with open(file, "r", encoding="utf8") as the_file:
        data = the_file.read().split("\n")
    return data


# Read the words for the avalanche test
words_for_avalanche = readFile("hashing/1000_words.txt")

# Perform the avalanche test
differences = avalanche_test(words_for_avalanche)

# Analyze the differences (e.g., calculate average, standard deviation)
average_difference = sum(differences) / len(differences)
print("Average bit difference (Avalanche Test):", average_difference)

# Plotting the bit differences
plt.plot(differences)
plt.title('Bit differences for words with a 1 bit difference\
in them (Avalanche Test)')
plt.xlabel('Index of compared pair')
plt.ylabel('The bit difference')
plt.show()

# Read the words for the uniformity test
words_for_uniformity = readFile("hashing/2000_random_words.txt")

# Perform the uniformity test
frequency = uniformity_test(words_for_uniformity)

# Plot the frequency of each hash value
plt.bar(frequency.keys(), frequency.values())
plt.title('Frequency distribution of hash values (Uniformity Test)')
plt.xlabel('Hash Value')
plt.ylabel('Frequency')
plt.show()
