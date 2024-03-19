import matplotlib.pyplot as plt
import os

list_size = 256

buckets = [[] for i in range (list_size)]


def get_hash(word):
    hash_value = 0 
    for letter in word:
        hash_value += ord(letter)
    return hash_value % list_size

def add(word):
    hash = get_hash(word)
    
    if word not in buckets[hash]:
        buckets[hash].append(word)

#this function used in the first and second test to draw the results of the tests
def plot (freq):
    plt.bar(freq.keys(), freq.values())
    plt.show()

#the first test function
def first_test():

    file_path = os.getcwd()
    file_path += "\\task 6\\random_words.txt"

    with open(file_path, "r")as file:
        file1 = file.read().split("\n")
        for i in file1:
            add(i)
    #a dic to set in the value of the lenght of each bucket
    dic= {}
    for i in range(len(buckets)):
        dic.setdefault(i, len(buckets[i]))

    plot(dic)

def second_test():
    #collecting the words from the similar words file 
    
    file_path = os.getcwd()  #the path pointing to the current folder
    file_path += "\\task 6\\similar_words.txt"
    with open(file_path, 'r') as file:
        words = []
        for line in file:
            for word in line.split():
                words.append(word)
    dic = {}
    
    for i in range(len(words) -1): #we don't use the last item (will be used already as a pair with the previous one)
        diff_value = abs(get_hash(words[i]) - get_hash(words[i +1])) #only intressted in the value of the difference 
        dic.setdefault(i, diff_value)
    plot(dic)


#the main method
def main():
    user_input = int(input("enter 1 for first test, or 2 for the second: "))
    if user_input == 1:
        first_test()
    elif user_input == 2: 
        second_test()
    else:
        print("wrong choice!")

main()
