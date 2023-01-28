def uniquelist(data1):
    x = []
    for s in data1:
      if s not in x:
        x.append(s)
    return x
datalist = []
n = int(input("enter elenents in a list "))
for k in range (n):
      data1 = int(input("enter in data list:"))
      datalist.append(data1)

print("orignal list",datalist)
print("uniquelist(datalist)")