value1 = input("Enter the first value")
value2 = input("Enter the second value")
value3 = input("Enter the third value")
list1 = [value1,value2,value3]
list1.append("Code is life")

value4 = input("Enter the 4th value")
value5 = input("Enter the 5th value")
value6 = input("Enter the 6th value")
list2 = [value4,value5,value6]
list2.append("python")

list1.extend(list2)
print(list1)