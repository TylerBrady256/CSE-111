#Tyler Brady Esteem project 

# I feel that I am a person of worth, at least on an equal plane with others.
# I feel that I have a number of good qualities.
# All in all, I am inclined to feel that I am a failure.
# I am able to do things as well as most other people.
# I feel I do not have much to be proud of.
# I take a positive attitude toward myself.
# On the whole, I am satisfied with myself.
# I wish I could have more respect for myself.
# I certainly feel useless at times.
# At times I think I am no good at all.

questions_to_ask = [{1,"I feel that I am a person of worth, at least on an equal plane with others."}
,{1,"I feel that I have a number of good qualities."}
,{0,"All in all, I am inclined to feel that I am a failure."}
,{1,"I am able to do things as well as most other people."}
,{0,"I feel I do not have much to be proud of."}
,{1,"I take a positive attitude toward myself."}
,{1,"On the whole, I am satisfied with myself."}
,{0,"I wish I could have more respect for myself."}
,{0,"I certainly feel useless at times."}
,{0,"At times I think I am no good at all."}]




def main():
    print_operation()
    points = score_questions()

    print(f"your score is {points}")

def score_questions(cumulative_score = 0):
    for number,question in questions_to_ask:
        print(f"\n{question}")
        answer = input("What is your answer D,d,a,or A ")
        cumulative_score +=score(answer,number)

    return cumulative_score

def score(answer,positive_negative):
# Strongly Disagree	0
# Disagree	1
# Agree	2
# Strongly Agree	3
    if positive_negative ==1:
        if answer == "A":
            points =3 
        elif answer =="a":
            points =2
        elif answer == "d":
            points = 1
        elif answer == "D":
            points = 0
        else:
            points = 0

    else: 
        if answer == "A":
            points =0 
        elif answer =="a":
            points =1
        elif answer == "d":
            points = 2
        elif answer == "D":
            points = 3
        else:
            points = 0
    

    real_points = points

    return real_points

def print_operation():
    print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
    print("This program will show you ten statements that you could possibly")
    print("apply to yourself. Please rate how much you agree with each of the")
    print(f"statements by responding with one of these four letters:\n")

    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print(f"A means you strongly agree with the statement.")



main()