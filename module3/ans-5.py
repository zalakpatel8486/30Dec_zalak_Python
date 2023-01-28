l1 = [10, 20, 30, 40, 50] 
l2 = [20, 30, 50, 40, 70] 
l3 = [50, 10, 30, 20, 40] 

l1.sort() 
l2.sort() 
l3.sort() 

if l1 == l2: 
    print ("The lists l1 and l2 are the same") 
else: 
    print ("The lists l1 and l2 are not the same") 

if l1 == l3: 
    print ("The lists l1 and l3 are the same") 
else: 
    print ("The lists l1 and l3 are not the same")