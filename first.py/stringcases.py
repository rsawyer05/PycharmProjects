# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice?

def stringcases(string):
    string2 = string.split()
    ' '.join(string2)
    return string.lower(), string.upper(), string.title(), string2[-1::-1]

