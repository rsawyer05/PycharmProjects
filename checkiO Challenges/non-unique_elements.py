#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list

def checkio(data):
    new_list = []
    num = len(data)
    if data.count(num) > 1:
        new_list.append(num)
        num -= 1

    data = new_list
    return data