question_prompts = [
    "what color are apples ? \na)black \nb)purple \nc)red",
    "what color are bananas ? \na)yellow \nb)pink \nc)white",
    "what color are watermelon ? \na)grey \nb)blue \nc)green", ]

class question:
    def __init__(self,prompt,ans):
        self.promt = prompt
        self.ans = ans

qcm = [question(question_prompts[0],"c"),
       question(question_prompts[1],"c"),
       question(question_prompts[2],"c")]

score = 0
for tries in qcm:
    answer = input(tries.promt + "\nwhat's the answer ? :")
    if answer == tries.ans:
        score +=1
print("you got " + str(score) + " out of " + str(len(question_prompts)))