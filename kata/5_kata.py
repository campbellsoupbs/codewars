#!/usr/bin/python3

#Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
#The first word within the output should be capitalized only if the original word was capitalized
#(known as Upper Camel Case, also often referred to as Pascal case).

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    if len(text) == 0:
        return text
    else:
        word_list = re.split('-|_', text)
        answer_list = []
        if word_list[0][0].isupper() == False:
            answer_list.append(word_list[0])
            for word in word_list[1:]:
                word = word.capitalize()
                answer_list.append(word)
        else:
            for word in word_list:
                word = word.capitalize()
                answer_list.append(word)
        return ''.join(answer_list)

#Hmm probably a better way to do this..