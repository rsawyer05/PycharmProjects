def members(my_dict, my_list):

    in_list_and_dict = 0

    for key in my_list:
        if key in my_dict:
            in_list_and_dict += 1

    return in_list_and_dict
