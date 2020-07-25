
























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