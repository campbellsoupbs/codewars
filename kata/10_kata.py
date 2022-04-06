#!/usr/bin/python3

"""""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway 
"""""

def pig_it(text):
    wlist = text.split()
    piglist = []
    for word in wlist:
        if word.isalpha() == True:
            piglist.append(f'{word[1:]}{word[0]}{"ay"}')
        else:
            piglist.append(word)
    return " ".join(piglist)