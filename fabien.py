import random

print("Welcome to Roki Game!!")
print("Hello world")

choices = ['rock','paper','scissors']

score=0
comp_score=0
rounds=1
game_over=False
while game_over==False:
    print("Round",rounds,"FIGHT!!!!!")
    ur_choice = input("Choose r for Rock, p for paper or s for scissors: ")
    comp_choice = choices[random.randint(0,2)]
    if comp_choice=='rock':
        if ur_choice=='r':
            print("\nComputer chose",comp_choice)
            print("It's tie!!\n")
            rounds +=1 
        elif ur_choice=='s':
            comp_score += 1
            print("\nComputer chose",comp_choice)
            print("You loose!!\n")
            print("Computer score is:",comp_score)
            rounds +=1
        else:
            if ur_choice=='p':
                score += 1
                print("\nComputer chose",comp_choice)
                print("You win!!\n")
                print("Your score is:",score)
                rounds +=1
            else:
                print("Invalid choice\n")
    elif comp_choice=='paper':
        if ur_choice=='p':
            print("\nComputer chose",comp_choice)
            print("It's tie!!\n")
            rounds +=1
        elif ur_choice=='r':
            comp_score += 1
            print("\nComputer chose",comp_choice)
            print("You loose!!\n")
            print("Computer score is:",comp_score)
            rounds +=1
            
        else:
            if ur_choice=='s':
                print("\nComputer chose",comp_choice)
                print("You win!!\n")
                print("Your score is:",socre)
                rounds +=1
                score += 1
            else:
                print("Invalid choice\n")
    else:
        if ur_choice=='s':
            print("\nComputer chose",comp_choice)
            print("It's tie!!\n")
            rounds +=1
        elif ur_choice=='p':
            comp_score += 1
            print("\nComputer chose",comp_choice)
            print("You loose!!\n")
            print("Computer score is:",comp_score)
            rounds +=1
        else:
            if ur_choice=='r':
                print("\nComputer chose",comp_choice)
                print("You win!!\n")
                print("Your score is:",score)
                rounds +=1
                score += 1
            else:
                print("Invalid choice\n")
    if score==3:
        game_over=True
        print("\nYou win Congrats")
    if comp_score==3:
        game_over=True
        print("\nYou loose")
    
            
