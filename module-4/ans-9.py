f4=open('myfile.txt',"r")
data=f4.read()
f4.close()
sepcial_char = "nine,four"
for schar in sepcial_char:
    if schar in data:
        data = data.replace(schar,"")
  

word_list = data.split()
word_count ={}
for word in word_list:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
for key,value in word_count.items():
    print(f"{key} t: {value}")

