#!/usr/bin/python3 

# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).

def is_pangram(s):
    letter_dic = {}
    ls = s.lower()
    for letter in ls:
        if letter.isalpha() == True:
            letter_dic[letter] = letter_dic.get(letter, 0) +1                  #Create histogram for each letter in sentence
    if len(letter_dic) == 26:                                                  #If histogram has 26 letters, sentence is a pangram (True)
        return True
    return False


#Alt/better way:

# def is_pangram(s):
#     s = s.lower()
#     for char in 'abcdefghijklmnopqrstuvwxyz':
#         if char not in s:
#             return False
#     return True
