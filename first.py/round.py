# The first half of the string, rounded with round(), should be lowercased.
# The second half should be uppercased.
# E.g. "Treehouse" should come back as "treeHOUSE"

def sillycase(item):
    item = 'Treehouse'
    lower_case = item[:round(len(item) / 2)].lower()
    upper_case = item[-(len(item) - (round(len(item) / 2))):].upper()

    result lower_case + upper_case


