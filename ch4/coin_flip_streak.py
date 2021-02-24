#! python3

"""
https://automatetheboringstuff.com/2e/chapter4/
Automate the Boring Stuff Chapter 4 Practice Project:
Coin Flip Streaks
"""

import random


def coin_flipper(num):
    flips = []                      # list to track results
    for i in range(num):
        if random.randint(0, 1):    # 1 heads, 0 tails
            flips.append("H")
        else:
            flips.append("T")
    string_results = "".join(flips) # convert to a single string to search for streaks
    return string_results

def streak_check(experiments, streak):
    """
    If you ever want to try a negative progression betting strategy play with this first...
    :param experiments: number of experiments to run, 10000 recommended
    :param streak: length of streak to check
    :return: results of experiment
    """
    count = 0
    for rounds in range(experiments):
        results = coin_flipper(100)
        if ("H" * streak) in results:
            count += 1
        elif ("T" * streak) in results:
            count += 1
    print("A streak of at least {} occurred approximately {}% of the experiments.".format(streak, (count/experiments)*100))

streak_check(10000, 6)