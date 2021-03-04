import pyinputplus as pyip
import random, time


numberOfQuestions = 10
correct = 0

for q in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = "#%s: %s x %s =" % (q+1, num1, num2)
    try:
        # correct answers handled by allowRegexes
        # incorrect by blockRegexes, with custom message
        pyip.inputStr(prompt, allowRegexes=["^%s$" % (num1 * num2)],
                      blockRegexes=[(".*", "Incorrect!")],
                      timeout=8, limit=3)
    except pyip.RetryLimitException:
        print("Too many tries!")
    except pyip.TimeoutException:
        print("Times up!")
    else:
        print("Correct!")
        correct += 1
    time.sleep(1)

print("You got {} out of {}".format(correct, numberOfQuestions))