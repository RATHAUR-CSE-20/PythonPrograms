M1=int(input("Enter Marks Of Maths : "))
M2=int(input("Enter Marks Of Science : "))
M3=int(input("Enter Marks Of English : "))
if(M1<33 or M2<33 or M3<33):
    print("You Failed")
elif(M1+M2+M3)/3 <40 :
    print("You Failed")
else:
    print("Congratulation!! You Passed")
print("Thanks For Using My Program")
N=input(print("Press Enter To Exit"))