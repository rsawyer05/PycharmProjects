# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.

def combo(num, letter):
  output = []
  for index, value in enumerate(num):
    output.append((value, letter[index]))

  return output
