D={"Book":"It Is a Sea Of Knowledge",
    "Harshit":"A Coder",
    "Shubham":"Harshit Friend"
}
print(list(D.keys())) #print keys of dictionary
print(D.values()) # print values of list
print(D.items()) # print the keys,value for all contents of dictionary
print(D)
UD={
    "Lovish":"Friend" #It Is Updated dictionary
}
D.update(UD) #It Updates The Dictionary
print(D)
print(D.get("Harshit"))