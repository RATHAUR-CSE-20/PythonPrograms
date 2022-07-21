def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[45,46,47,48]
percentage1=percent(marks1)
marks2=[51,56,57,58]
percentage2=percent(marks2)
print(percentage1, percentage2)
E=input("Press Enter To Exit")
