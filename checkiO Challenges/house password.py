import re




def checkio(data):
    upper = False
    lower = False
    number = False
    letter = False

    for letter in data:
        if letter.isupper():
            if upper == True:
                continue
        else:
            upper = True

    for letter in data:
        if letter.islower():
            if lower == True:
                continue
        else:
            lower = True

    for letter in data:
        if letter.isnumeric():
            if number == True:
                continue
        else:
            number = True

    if len(data) >= 10:
        length = True

    if upper and lower and number and length == True:
        return True
    else:
        return False


checkio('kdjdhfyHY6')