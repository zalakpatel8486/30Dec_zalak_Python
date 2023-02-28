n=int(input('enter the n lines:'))
f=open('myfile.txt','r')
for line in (f.readlines()[n]):
    print(line,end="")
f.close()
