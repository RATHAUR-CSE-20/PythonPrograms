f = open('Poem.txt')
t =f.read()
if 'Twinkle' in t:
    print("Twinkle is Present")
else:
    print("Twinkle is Not Present")
f.close()