#! python3

# Automate the Boring Stuff Ch 9 Project
# Creates state capital quizzes and corresponding answer key
# Question order / options randomized

import random

CAPITALS = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

for quizNum in range(35):
    # Create quiz and answer key files
    quizFile = open(f"quiz\capitalsquiz_{quizNum + 1}.txt", "w")
    answerKeyFile = open(f"quiz\capitalsquiz_answers {quizNum + 1}.txt", "w")

    # Write out the header for the quiz
    quizFile.write("Name:\n\nDate:\n\nPeriod\n\n")
    quizFile.write(f"State Capitals Quiz (Form {quizNum + 1})".center(40))
    quizFile.write("\n\n")

    # Shuffle order of states
    states = list(CAPITALS.keys())
    random.shuffle(states)

    # Loop through all 50 states, making question for each
    for questionNum in range(50):
        correct = CAPITALS[states[questionNum]]
        wrong = list(CAPITALS.values())
        del wrong[wrong.index(correct)]
        wrong = random.sample(wrong, 3)
        choices = wrong + [correct]
        random.shuffle(choices)

        quizFile.write(f"{questionNum + 1}) What is the capital of {states[questionNum]}?\n")
        for i in range(4):
            quizFile.write(f"     {'ABCD'[i]}. { choices[i]}\n")
            quizFile.write("\n")

        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[choices.index(correct)]}\n\n")

    quizFile.close()
    answerKeyFile.close()