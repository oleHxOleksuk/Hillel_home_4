
lst = range(10)
numbers = []
new_list = []
for el in lst:
    numbers.append(el)

new_list.append(numbers[0])
new_list.append(numbers[2])
new_list.append(numbers[-2])

print(numbers,'=>',new_list )
