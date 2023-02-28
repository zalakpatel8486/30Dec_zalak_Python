n=int(input('enter the value of n'))
f=open('myfile.txt','r')
s=f.read()
list=s.split()
for i in list:
    if(len(i)>n):
        print(i)