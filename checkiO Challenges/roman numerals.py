# I 1 (unus)
# V 5 (quinque)
# X 10 (decem)
# L 50 (quinquaginta)
# C 100 (centum)
# D 500 (quingenti)
# M 1,000 (mille)

# verify number is larger than roman numberal
# subtract roman numeral value from number
# add roman numeral to output string
# compare number to all roman numerals and add to output string
# return output string


def checkio(data):
    number = data
    roman = ""
    while number != 0:
        if number >= 1000:
            number -= 1000
            roman += 'M'
        elif number >= 500 < 1000:
            number -= 500
            roman += 'D'
        elif number >= 100 < 500:
            number -= 100
            roman += 'C'
        elif number >= 50 < 100:
            number -= 50
            roman += 'L'
        elif number >= 10 < 50:
            number -= 10
            roman += 'X'
        elif number >= 5 < 10:
            number -= 5
            roman += 'V'
        elif number == 4:
            number -= 4
            roman += 'IV'
        elif number >= 1 < 4:
            number -= 1
            roman += 'I'
    #replace this for solution
    print(roman, data)

checkio(2016)