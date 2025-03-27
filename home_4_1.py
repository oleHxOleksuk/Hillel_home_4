#lst = [0, 1, 0, 12,0, 3]
#lst = [0]
#lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
zero_list = []
for el in lst:
    zero_list.append(0)
    lst.remove(0)
lst.extend(zero_list)
print(lst)







