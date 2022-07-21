def remove_and_split(string, word):
    newstr= string.replace(word, "")
    return newstr.strip()
this = "     Harshit Is Good     "
n = remove_and_split(this, "Harry")
print(n)
