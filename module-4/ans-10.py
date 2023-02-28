number = ['two', 'three', 'four', 'five', 'six', 'seven']

with open('myfile.txt', "w") as file:
        for c in number:
                file.write("%s\n" % c)

content = open('myfile.txt')
print(content.read())
