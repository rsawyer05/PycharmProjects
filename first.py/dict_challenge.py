# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.

def word_count(string):
    woodchuck_dict = {}

    for word in string.split():

        if word in woodchuck_dict:
            woodchuck_dict[word] += 1
        else:
            woodchuck_dict[word] = 1
    print(woodchuck_dict)


word_count("how much wood could a woodchuck chuck if a woodchuck could chuck wood")
