import re

def checkio(text):
    new_dict = {}
    text1 = re.findall(r'[a-zA-Z]', text)
    for letter in text1:

        if letter in new_dict:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1

    print(new_dict)
    key_with_max_val(new_dict)

def key_with_max_val(dict):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    unsorted_dict = (max(dict, key=dict.get))
    print(unsorted_dict)

    print(sorted(dict, key=str.lower))

checkio("a" * 9000 + "b !" * 9000 + "c" * 4000) == "a", "Long."

#if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert checkio("Hello World!") == "l", "Hello test"
#    assert checkio("How do you do?") == "o", "O is most wanted"
#    assert checkio("One") == "e", "All letter only once."
#    assert checkio("Oops!") == "o", "Don't forget about lower case."
#    assert checkio("AAaooo!!!!") == "a", "Only letters."
#    assert checkio("abe") == "a", "The First."
#    print("Start the long test")
#    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
#    print("The local tests are done.")


