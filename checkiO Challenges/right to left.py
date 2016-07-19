def left_join(phrases):
    new_list = ','.join(phrases)
    return new_list.replace("right", "left")
