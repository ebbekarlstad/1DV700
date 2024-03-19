import matplotlib.pyplot as plt
from operator import itemgetter

def get_hash(word):
        values = 0  # hash of a word
        count = 0
        for character in word:
            count += 1
            values += ord(character) * (count + 303)
        hashed = values % 256
        return hashed

def readFile(file):
    with open(file, "r", encoding="utf8") as the_file:
        data = the_file.read().split("\n")
    return data


def hash_avalanch(file):
    dict = {}
    for words in file:
        hashh = get_hash(words)
        dict[words] = hashh

    dic_list = sorted(dict.items())
    return dic_list

def hash_collision(file):
     
    dict = {}
    list = []
    for words in file:
        theHash = get_hash(words)
        list.append(theHash)
    for x in list:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    dict_list = sorted(dict.items())
    return dict_list



def plotLine(list, title):
    X = []
    Y = []
    for x in list:
        if len(X) and len(Y) == 10:
            break
        else:
            X.append(x[0])
            Y.append(x[1])

    # plot chart
    plt.plot(X, Y)
    plt.title(title)
    plt.xlabel("Strings")
    plt.ylabel("The Hash Values")
    
    plt.show()

def plotBar(file, title):
    X = []
    Y = []
    for x in file:
        X.append(x[0])
        Y.append(x[1])

    # plot chart
    plt.bar(X, Y)
    plt.title(title)
    plt.xlabel("Number of hashes")
    plt.ylabel("The frequency of reaccuring hashes")
    
    plt.show()
    
    

file = readFile("google-10000-english.txt")
dic_lst = hash_collision(file)
plotBar(dic_lst, "Random String")

# One bit different strings
file = readFile("one_bit_words.txt")
dic_lst = hash_avalanch(file)
plotLine(dic_lst, "One bit different strings")