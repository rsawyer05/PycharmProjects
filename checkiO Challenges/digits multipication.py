from functools import reduce

def checkio(number):
    new_list = []
    number_as_string = str(number)
    for num in number_as_string:
        if num != '0':
            new_list.append(int(num))

    sum = reduce(lambda a, x: a * x, new_list)
    print(sum)
checkio(1230460)
