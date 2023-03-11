f=open("myfile.txt","r")
f1=open("text2.txt","w")
for i in f:
    f1.write(i)