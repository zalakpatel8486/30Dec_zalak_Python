def count (string):

    dict = {}
    w = string.split()

    for i in w :
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict
a = input("enter a sentence:")
print(count(a))


