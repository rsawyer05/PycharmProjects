dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]


string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts, string):
    list = []
    for food_name in dicts:
        list.append(string.format(**food_name))

    return list

