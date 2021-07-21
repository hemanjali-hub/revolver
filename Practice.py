list1 = [2, 4, 1, 1, 3, 7, 7, 8, 3, 6]
exist_count=0
for x in list1:
    exist_count=list1.count(x)
    if exist_count>1:
        list1.remove(x)
print(list1)
list2 = [11, 5, 17, 18, 23]
total=list2[0]
for x in range(1,len(list2)):
    total=total*list2[x]
print(total)
list3 = [11, 5, 17, 18, 23]
first_large=list3[0]
sec_large=None
for x in list3[1:]:
    if x>first_large:
        first_large=x
    elif sec_large==None or sec_large<x:
         sec_large = x

print(first_large)
print(sec_large)






