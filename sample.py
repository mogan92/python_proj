mylist = [3 , 7 , 10 , 14 , 18 , 13 , 20 , 21 , 34 , 39]

mylist_even=[]

mylist_odd=[]

for item in mylist:
    if item % 2 == 0:
        mylist_even.append(item)
    else:
        mylist_odd.append(item)

print(mylist_even)

print(mylist_odd)

print("program successfully executed")
