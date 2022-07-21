with open('Another.txt') as f:
    content = f.read()

content = content.replace("Donkey", "$%^@$^#")

with open("Another.txt", 'w') as f:
    content = f.read()