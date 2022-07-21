N=int(input("Enter Any Number: "))
 # Fact=1
# for i in range(N):
#     Fact=Fact*(i+1)
# print(Fact)
print("************************************")
def Factorial_iter(N):
    Fact=1
    for i in range(N):
        Fact = Fact*(i+1)
    return Fact

F = Factorial_iter(N)
print("Factorial is",F)
print("************************************")
def Fact_Recursive(N):
    return N * Fact_Recursive(N-1)
F=Factorial_iter(N)
print("Factorial Using Recursion",F)
print("************************************")
A=input("Press Enter To Exit ")