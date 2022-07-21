# SNAKE , WATER & GUN GAME CREATED BY HARSHIT RATHAUR
import random

def gameWin(comp, you):
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return  True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


randNo = random.randint(1, 3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo:
    comp='g'
you= input("Player's Turn: ( Snake(s) Water(w) or Gun(g)? ): ")
a = gameWin(comp, you)
print(f"Computer Choose {comp}")
print(f"You Choose {you}")
if a ==None:
    print("Game Is Tie")
elif a:
    print("Congratulation!! You Win")
else:
    print("You Lose")
print("************************************************")
E=input("Press Enter To Exit: ")