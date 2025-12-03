questions = {
    "What does 'FG' stand for": "Fictional Googology",
    "Am i bad at coding": "Yes",
    "BBN Stands for what": "Big Boi Numbers",
}

score = 0

for question, answer in questions.items():
 user_answer = input(question + " ").strip().capitalize()
 if user_answer == answer:
     print("Correct! You win nothing of value")
else:
    print("Incorrect! but the correct one was something like {answer}")

print(f"final score: {score}/{len(questions)}")
