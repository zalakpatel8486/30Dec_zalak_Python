L = [{"1":"S001"}, {"2": "S002"}, {"3": "S001"}, {"4": "S005"}, {"5":"S005"}, {"6":"S009"},{"7":"S007"}]
print("Original List: ",L)
a1 = set( val for dic in L for val in dic.values())
print("Unique Values: ",a1)
