import random
lst = range(random.randrange(3, 11))
#lst = range(7)
#lst = range(3)
numbers = []
new_list = []
for el in lst:
    numbers.append(el)

new_list.append(numbers[0])
new_list.append(numbers[2])
new_list.append(numbers[-2])

print(numbers,'=>',new_list )




