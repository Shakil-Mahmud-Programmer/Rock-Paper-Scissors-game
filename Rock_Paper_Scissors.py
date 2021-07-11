import random,colorama
from colorama import Fore,Back,Style
colorama.init()
my_score=machine_score=drow=0
round=1
print("\033[31m"+"Type exit for escape !")
while True:
    choice = ['rock', 'paper', 'scissors']
    machine = random.choice(choice)
    print("\033[34m"+"Round= ",round)
    round=round+1
    me=input("\033[32m"+"Your choice: ")
    print("\033[36m"+"Machine choice: ",machine)
    me=me.lower()
    if machine==me:
        print("\033[36m"+"Draw")
        drow=drow+1
    elif machine=='rock' and me=='scissors':
        print("\033[31m"+"machine won")
        machine_score=machine_score+1
    elif machine=='rock' and me=='paper':
        print("\033[32m"+'you won')
        my_score=my_score+1
    elif machine=='paper' and me=='scissors':
        print("\033[32m"+'you won')
        my_score = my_score+1
    elif machine == 'paper' and me == 'rock':
        print("\033[31m"+'machine won')
        machine_score = machine_score+1
    elif machine == 'scissors' and me == 'paper':
        print("\033[31m"+'machine won')
        machine_score = machine_score+1
    elif machine == 'scissors' and me == 'rock':
        print("\033[32m"+'You won')
        my_score = my_score+1
    elif me=='exit':
        round=round-2
        print("\n\n"+"\033[31m"+"<=============>")
        print("\033[34m"+"Total Round= ",round)
        print("\033[34m"+"Drow time= ",drow)
        print("\033[34m"+"Your Score= ",my_score)
        print("\033[34m"+"Machine Score=",machine_score)
        if my_score>machine_score:
            print("\033[32m"+"Congratulation ! You Won the Game !")
        elif my_score==machine_score:
            print("\033[36m" + "Its a Draw !")
        else:
            print("\033[31m"+"Sorry ! Machine Won the Game !")
        print("\033[31m" + "<=============>")
        print("\n"+"\033[34m"+"Thanks from Shakil Mahmud for playing !")
        break
    print("\n")




