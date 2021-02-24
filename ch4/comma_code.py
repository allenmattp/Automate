#! python3

"""
https://automatetheboringstuff.com/2e/chapter4/
Automate the Boring Stuff Chapter 4 Practice Project:
Comma Code
"""
spam = ['apples', 'bananas', 'tofu', 'cats']
list = [1, 2, 3, 4, 5, 6]
empty = []

def comma_code(list):
    string = ""
    for i in range(len(list)):
        if i != (len(list) - 1):
            string += str(list[i]) + ", "
        else:
            string += "and " + str(list[i])
    print(string)

comma_code(spam)
comma_code(list)
comma_code(empty)