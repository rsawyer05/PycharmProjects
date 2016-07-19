the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
value = the_list.pop(-3)
the_list.insert(0,1)

the_list.remove(False)
del the_list[1]
del the_list[3]
the_list.extend(range(4, 21))

print(the_list)