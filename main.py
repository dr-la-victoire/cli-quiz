"""This is a quiz...
The user will be shown some multiple choice questions.
When an answer is selected, it gives feedback on the score.
It writes the score in a file and gives feedback on where the user stands!"""

import requests, json, time, random

r = requests.get("https://opentdb.com/api.php?amount=10&category=32")
response = r.json()

# getting the questions from the response
questions = response["results"]
stored = {}
# counter = 0

for q in questions:
    answers = [q["correct_answer"]] + q["incorrect_answers"]
    random.shuffle(answers)

    stored[q["question"]] = {"options": answers, "correct": q["correct_answer"]}


# Turning this into a viable quiz program
print("Welcome to the super awesome CLI Quiz program")
time.sleep(3)
print("Let's begin!")

# mapping the answers to options
default_labels = ["A", "B", "C", "D"]
# keeping score
score = 0

for question, data in stored.items():
    print(f"Question: {question}")

    for index, answer in enumerate(data["options"]):
        print(f"{default_labels[index]}. {answer}")

    user_answer = input("What is your final answer?: ")
    time.sleep(3)

    # condition to check whether or not the answer is correct
    if user_answer == data["correct"]:
        print("You are correct")
        score = score + 1
    else:
        print("You are wrong")
        print(f"Correct answer: {data['correct']}\n")
    time.sleep(3)

print(f"You scored {score} points in the end!")
