f3=open('myfile.txt','r')
count=0
for line in f3:
    words=line.split(" ")
    count= len(words)
f3.close()
print("number of words in a text file : ",count)
