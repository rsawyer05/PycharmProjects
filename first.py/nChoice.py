import random

def nchoices(iterable, n):


    results = []
    for index in range(n): #<-- Add loop to run "n" times
        # pick random item
        pick = random.choice(iterable)
        # append pick to results list
        results.append(pick) #<-- in each loop, choose random item from "iterable" and append to results list
    # after looping complete, return results list
    return results