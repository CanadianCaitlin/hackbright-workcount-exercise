

# define a function that takes in file as a parameter
# open the file
# create empty dictionary
# loop through file by line
    # split line by space and rstripe
    # for word in line
    # check to see if the word is in the dictionary
        # if the word is in dictionary, increase the count by 1
        # if the word is not in the dictionary, add word to dictionary
# return dictionary items

def word_count(filename):
    file = open(filename)
    word_dictionary = {}
    for line in file:
        list = line.rstrip().split(" ")
        for word in list:
            word_dictionary[word] = word_dictionary.get()


    return word_dictionary.items()




















# def count_words(file):
#     # return dictionary of words and the # of times they appear in text

#     word_counts = {} 
#     for line in file:
#         line = line.rstrip().split(" ")
#         for word in line:
#             if "," in word or ("?" in word) or ("." in word):
#                 word = word[:-1]
#                 # print(word.lower())
#                 word_counts[word.lower()] = word_counts.get(word, 0) + 1

#             else:
#                 # print(word.lower())
#                 word_counts[word.lower()] = word_counts.get(word, 0) + 1
    
#     return word_counts

# test_file = open("test.txt")
# print(count_words(test_file))
# test_file.close()

# twain_file = open("twain.txt")
# print(count_words(twain_file))
# twain_file.close()