import random 

questions = (
    "How many genders are there?",
    "Which planet is the third most closest to the sun?",
    "Which continent is the most populus?",
    "Biology is the study of --------.",
    "How many bones and muscles are there in adult human respectively?"
)
options = (
    """
    A. Four 🤡
    B. Two 🗿
    C. 69 💀
    D. A lot 🤓
    """,
    """
    A. Mars
    B. Mercury
    C. Earth
    D. Jupiter
    """,
    """
    A. Asia
    B. Africa
    C. Europe
    D. North America
    """,
    """
    A. Physical and Chemical properties of matters.
    B. Solar system and the universe.
    C. Living things and organisms.
    D. Geographical and historical events.
    """,
    """
    A. 208 and 1200
    B. 206 and 600 
    C. 600 and 206
    D. 1200 and 208
    """
)
correct_answers = ("B", "C", "A", "C", "B")
question_num = 1
score = 0
random_num_lists = random.sample(range(0,5), 5)
for i, x in enumerate(random_num_lists):
    print(f"{question_num}. {questions[random_num_lists[i]]}")
    print(options[random_num_lists[i]])
    user_answer = input("Enter ur answer in the form of A, B, C, D: ").upper()
    if correct_answers[random_num_lists[i]] == user_answer:
        print("You are correct!")
        score += 1
    else:
        print(f"Incorrect! The answer is {correct_answers[random_num_lists[i]]}")
    question_num += 1
if score <= 2:
    print(f"You got {score}/5! Disappointing!")
elif score == 3:
    print(f"You got {score}/5! Fair enough!")
elif score == 4:
    print(f"You got {score}/5! Very good!")
else:
    print(f"You aced it {score}/5! Excellent!")

