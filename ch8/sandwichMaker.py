import pyinputplus as pyip

# available choices
bread = ["wheat", "white", "sourdough"]
protein = ["chicken", "turkey", "ham", "tofu"]
cheese = ["cheddar", "Swiss", "mozzarella"]
extras = ["mayo", "mustard", "lettuce", "tomato"]

# get inputs
breadChoice = pyip.inputMenu(bread, "What type of bread?\n")
proteinChoice = pyip.inputMenu(protein, "What type of protein?\n")
cheeseChoice = pyip.inputYesNo("cheese? ")

if cheeseChoice == "yes":
    cheeseChoice = pyip.inputMenu(cheese, "What type of cheese?\n")
else:
    cheeseChoice = "no cheese"

extrasList = []
for e in extras:
    extrasChoice = pyip.inputYesNo(e + "? ")
    if extrasChoice == "yes":
        extrasList.append(e)

# make selections into strings for later
if len(extrasList):
    extrasChoice = ", ".join(extrasList)
else:
    extrasChoice = "no extras"

# figure out the price
price = 0
if proteinChoice == "ham":
    price += 5.
else:
    price += 4.

if cheeseChoice != "no cheese":
    price += .5

# print sandwich ordered + price
print("{} {} on {} with {}. Your total is ${}.".format(proteinChoice, cheeseChoice, breadChoice, extrasChoice, round(price, 2)))