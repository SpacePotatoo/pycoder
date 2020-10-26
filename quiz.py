"""
@Author: Ayuta
Description: a simple quiz
"""
import sys

subjects = ["History", "history", "Geography", "geography", "Science", "science", "q", "Q"]
options = ["A", "B", "C", "D", "Q", "q"]
score=0

print("Hello! Welcome to my quiz!\nAnswer the questions by only typing capital letters.\n")

quiz = ""
while quiz not in subjects:
    quiz = input("Which Quiz do you want to attempt?\nHistory/Geography/Science\npress Q anytime to exit\n>>")
    if quiz == "History" or quiz == "history" or quiz == "Geography" or quiz == "geography" or quiz == "Science" or quiz == "science":
        print("\nAnswer the following questions-\n")
    elif quiz == "q" or quiz == "Q":
        print("/nGoodbye!")
        sys.exit()
    else:
        print("Invalid Input\n")

if quiz == "History" or quiz == "history" :
    ans1 = ""
    while ans1 not in options:
        ans1 = input("Do or Die slogan is associated with:\nA. Mahatma Gandhi\nB. Bal Gangadhar Tilak\nC. Jawarharlal Nehru\nD. Subhash Chandra Bose\n>>")
        if ans1 == "A":
            print("\nGood!\n")
            score += 1
        elif ans1 == "B" or ans1 == "C" or ans1 == "D":
            print("\nWrong! Correct answer is Mahatma Gandhi.\n")
        elif ans1 == "Q" or ans1 == "q":
            print("Goodbye!")
            sys.exit()
        else:
            print("\nAnswer the questions only with A, B, C, or D.")
            
    ans2 = ""
    while ans2 not in options:
        ans2 = input("The Indian National Congress was founded by:\nA. Mahatma Gandhi\nB. Annie Besant\nC. W.C.Bannerji\nD. A.O.Hume\n>>")
        if ans2 == "D":
            print("\nGood!\n")
            score += 1 
        elif ans2 == "A" or ans2 == "B" or ans2 == "C":
            print("\nWrong! Correct answer is A.O.Hume.\n")
        elif ans2 == "Q" or ans2 == "q":
            print("Goodbye!")
            sys.exit()
        else:
            print("\nAnswer the questions only with A, B, C, or D.")
            
    ans3 = ""
    while ans3 not in options: 
        ans3 = input("The Civil services in India was established by\nA. Lord Rippon\nB. Lord Dalhousie\nC. Lord William Bentick\nD. Lord Cornwallis\n>>")
        if ans3 == "A":
            print("\nGood!\n")
            score += 1
        elif ans3 == "B" or ans3 == "C" or ans3 == "D":
            print("\nWrong! Correct answer is Lord Rippon.\n")
        elif ans3 == "Q" or ans3 == "q":
            print("Goodbye!")
            sys.exit()
        else:
            print("\nAnswer the questions only with A, B, C, or D.")
            
    ans4 = ""
    while ans4 not in options:
        ans4 = input("In the Battle of Wandiwash, the English defeated\nA. the Dutch\nB. the French\nC. the Portuguese\nD. None of these\n>>")
        if ans4 == "B":
            print("\nGood!\n")
            score += 1
        elif ans4 == "A" or ans4 == "C" or ans4 == "D":
            print("\nWrong! Correct answer is the french.\n")
        elif ans4 == "Q" or ans4 == "q":
            print("Goodbye!")
            sys.exit()
        else:
            print("\nAnswer the questions only with A, B, C, or D.")
            
    ans5 = ""
    while ans5 not in options:
        ans5 = input("The first ruler of Pala dynasty was\nA. Gopala\nB. Dharmapala\nC. Bhaskaravarman\nD. None of these\n>>")
        if ans5 == "A":
            print("\nGood!\n")
            score += 1
        elif ans5 == "B" or ans5 == "C" or ans5 == "D":
            print("\nWrong! Correct answer is Gopala.\n")
        elif ans5 == "Q" or ans5 == "q":
            print("Goodbye!")
            sys.exit()
        else:
            print("\nAnswer the questions only with A, B, C, or D.")
            
    ans6 = ""
    while ans6 not in options:
        ans6 = input("The Aryans came from Central Asia to India around\nA. 8000 B.C.\nB. 6500 B.C.\nC. 3500 B.C.\nD. 2500 B.C.\n>>")
        if ans6 == "D":
            print("\nGood!\n")
            score += 1
        elif ans6 == "B" or ans6 == "C" or ans6 == "A":
            print("\nWrong! Correct answer is 2500 B.C.\n")
        elif ans6 == "Q" or ans5 == "q":
            print("Goodbye!")
            sys.exit()
        else: 
            print("\nAnswer the questions only with A, B, C, or D.")
         
    
    print("You got",score,"questions correct out of 6.")
            
            

sys.exit()
