# Make a quiz that has question with 4 option.
# Add 1 point if the answer is correct.
# Reduce 1 point if it is incorrect.
# Also it should have an option to skip a question and quit the quiz.
# Design the quiz using dictionaries.

quiz = {
    1: {
        "question": "hbvqwjrhgbqiuwbvbqw?",
        "options": {
            "a": "qweoiu",
            "b": "zxcmnv",
            "c": "plmokn",
            "d": "asdhjk"
        },
        "answer": "b"
    },
    2: {
        "question": "mznxvqwueiryttopa?",
        "options": {
            "a": "kjhgfd",
            "b": "poiuyt",
            "c": "lkjhgf",
            "d": "mnbvcx"
        },
        "answer": "c"
    },
    3: {
        "question": "qqwerrttyyuuiop?",
        "options": {
            "a": "vbnhyu",
            "b": "ertyui",
            "c": "sdfghj",
            "d": "xcvbnm"
        },
        "answer": "a"
    },
    4: {
        "question": "zzxxyywwvvuuttrr?",
        "options": {
            "a": "ghjklo",
            "b": "rewqaz",
            "c": "tyuigh",
            "d": "bnmert"
        },
        "answer": "c"
    }
}

score = 0

print("Enter a, b, c or d")
print("Enter s to skip")
print("Enter q to quit")

for question_no, data in quiz.items():
    print()
    print("Question", question_no)
    print(data["question"])

    for option_key, option_value in data["options"].items():
        print(option_key, ")", option_value)

    user_answer = input("Enter your answer: ").lower()

    if user_answer == "q":
        break
    elif user_answer == "s":
        continue
    elif user_answer == data["answer"]:
        score = score + 1
    else:
        score = score - 1

print("Final score:", score)
