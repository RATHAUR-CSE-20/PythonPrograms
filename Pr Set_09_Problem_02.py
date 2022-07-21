def game():
    return 1000
Score = game()
with open('High_Score.txt') as f:
    High_Score= int(f.read())

if High_Score<Score:
    with open('High_Score.txt','w') as f:
        f.write(str(Score))
E=input("Press Enter To Exit: ")