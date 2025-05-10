#Kaun Banega Crorepati
# Displays KBC-style questions,
# Uses a list to store questions and answers,
# Calculates and displays the final prize based on correct answers.

#basic program
question= [
    "Captial of India?", "PM of India", "National animal of india?"
]

answer= [
    "Delhi", "Narendra Modi", "Tiger"
]

correct_answer_price = 10000
prize =  0

for i in range(len(question)):
    print(question[i])
    user_answer= input("Your answer: ")
    
    if user_answer.strip().lower() == answer[i].lower():
        print("Correct Answer\n")
        prize = prize + correct_answer_price
    
    else: 
        print("Wrong Answer\n")
        break

print("Game Over")
print("You won", prize)


#Giving 4 options to user
question= [
    "Captial of India?", "PM of India", "National animal of india?"
]

options = [
    ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Rahul Gandhi", "B. Arvind Kejriwal", "C. Narendra Modi", "D. Amit Shah"],
    ["A. Tiger", "B. Lion", "C. Peacock", "D. Elephant"]
]

answer = ["B","C","A"]

price = 0
correct_answer_price = 10000

for u in range(len(question)):
    print("Welcome to KBC")
    print("Q " + str(u+1)+" "+ question[i])
    print("Options", options[u][0])
    print("Options", options[u][1])
    print("Options", options[u][2])
    print("Options", options[u][3])

    user_input = input("Enter the answer(A/B/C/D):" ).strip()
    if user_input == answer[u]:  
        print("Correct Answer\n") 
        price = price + correct_answer_price
    else:
        print("Wrong Answer")
        print("Correct answer was: " + answer[u]+ "\n")
        #break
print("Game Over!","You won", str(price))


#Replaced break with a print() statement so the loop continues even after a wrong answer.