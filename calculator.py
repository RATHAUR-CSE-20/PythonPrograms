print("******************************************************")
num1 = input("Enter first Number : ")
operator = input("What Do You Want To Do(+,-,*,/,%) : ")
num2 = input("Enter Second Number : ")
num1 = int(num1)
num2 = int(num2)
if operator == "+":
    print("Sum Is", str(num1 + num2))
elif operator == "-":
    print("Difference Is ",str(num1 - num2))
elif operator == "*":
    print("Product Is ",str(num1 * num2))
elif operator == "/":
    print("Quotient Is ",str(num1 / num2))
elif operator == "%":
    print("Remainder Is ",str(num1 % num2))
else:
    print("You Have Entered An Invalid Operator")

print("Hello I am Harshit Rathaur , Thanks For Using My Program.")
input("Enter Your Name : ")
print("******************************************************")