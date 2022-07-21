print("*********************************")
#Problem 01

Name=input("Enter Your Name : ")
print("Good Afternoon, " + Name)

print("*********************************")
#Problem 02

letter = """Dear <|NAME|>,
Greetings From ABC Coding Hub , We Are Happy To Inform You , You Are Selected


Thanks and Regards
Date: <|DATE|>
"""
Name1=input("Enter Your Name : ")
date=input("Enter Date : ")
letter = letter.replace("<|NAME|>", Name1)
letter = letter.replace("<|DATE|>", date)
print(letter)

print("*********************************")

#Problem 03
 
St="This Is A string With Double  Spaces"
doublespaces = St.find("  ")
print(doublespaces)

print("*********************************")
#Problem 04

doublespaces=St.replace("  ", "")
print(St)

print("*********************************")
#Problem 05

Letter = "Dear Harshit, You Are Nice! Thanks!"
print(Letter)
formatted_Letter = "Dear Harshit,\n\t You Are Nice! \n Thanks!"
print(formatted_Letter)

print("*********************************")

E=input("Press Enter To Exit")


