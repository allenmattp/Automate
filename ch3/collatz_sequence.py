#! python3

"""
https://automatetheboringstuff.com/2e/chapter3/
Automate the Boring Stuff Chapter 3 Practice Project
"""

def collatz(number):
    if not number % 2:
        print(number // 2)
        return number // 2
    elif number % 2:
        print(3 * number + 1)
        return 3 * number + 1

if __name__ == '__main__':
    user_int = 0
    while not user_int:
        try:
            user_int = int(input("Enter an integer to explore the Collatz sequence:\n"))
        except ValueError:
            print("Enter an INTEGER.")
    number = collatz(user_int)
    while number != 1:
        number = collatz(number)