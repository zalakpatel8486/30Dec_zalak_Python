a = input('enter the string')
b=a.split()
largest=len(b[0])
for i in b:
    if len(i)> largest:
        largest = len(i)
print('largest string length=', largest )
