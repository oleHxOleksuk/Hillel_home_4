lst = [0, 1, 7, 2, 4, 8]
#lst = [1, 3, 5]
#lst = [6]
#lst = []
#lst = [0]
result = 0

if len(lst):
    for el in lst:
        if lst.index(el) % 2 == 0:
            result += el
    result = result * lst[-1]
else:
    result = 0
print(lst, '=>', result)