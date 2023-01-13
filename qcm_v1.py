from classes import Answers

question_prompts = [
    "what color are apples ? \na)black \nb)purple \nc)red",
    "what color are bananas ? \na)yellow \nb)pink \nc)white",
    "what color are watermelon ? \na)grey \nb)blue \nc)green", ]
print(question_prompts[0])

question1 = input("the answer is :")
question1 = question1.lower()
while question1 != "a" and question1 != "b" and question1 != "c":
    question1 = input("i could not pick that up. you said the answer was :")
    question1 = question1.lower()

print(question_prompts[1])
question2 = input("the answer is :")
question2 = question2.lower()
while question2 != "a" and question2 != "b" and question2 != "c":
    question2 = input("i could not pick that up. you said the answer was :")
    question2 = question2.lower()

print(question_prompts[2])
question3 = input("the answer is :")
question3 = question3.lower()
while question3 != "a" and question3 != "b" and question3 != "c":
    question3 = input("i could not pick that up. you said the answer was :")
    question3 = question3.lower()

Answers1 = Answers(question1, question2, question3)
score = 0

if Answers1.answer == "c" :
    score += 1
if Answers1.answer2 == "a" :
    score += 1
if Answers1.answer3 == "c" :
    score += 1

print("your score is : " + str(score))
