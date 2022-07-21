A=int(input("Enter any Number: "))
Prime = True

for i in range(2, A):
    if (A%i == 0):
        Prime = False
        break
if Prime:
    print("Prime Number")
else:
    print("Not A Prime Number")
E=input("Press Enter To Exit")
