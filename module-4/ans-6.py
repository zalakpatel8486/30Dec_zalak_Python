with open('myfile.txt')as file:
    lines = file.readlines()
    lines = [line.rstrip()for line in lines]
print(lines)