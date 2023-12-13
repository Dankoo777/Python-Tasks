import random
lst1 = []
while True:
    try:
        n = int(input("Input number of nums:"))
    except ValueError:
        print("Not int!!!")
        continue
    if n < 30 or n > 100:
        print("Must be between 30 and 100")
        continue
    else:
        break
for i in range(n):
    num = random.randint(20,600)
    lst1.append(num)
print(f"List1: {lst1}")
count = 0
for num in lst1:
    ed = num % 10
    if ed % 2 == 0:
        count += 1
print(f"Number of element with (ed % 2 == 0): {count}")
lst_copy = lst1.copy()
lst_copy.sort()
print(f"Sorted List1: {lst_copy}")
min_num = 0
for num in lst_copy:
    if num % 7 == 3:
        min_num = num
        break
index_min = lst1.index(min_num)
print(f"Index of min num that (num % 7 == 3): {index_min}")
lst2 = [num for num in lst1 if (((num // 10) % 10) == 5) or (((num // 100) % 10) == 3)]
print(f"List2: {lst2}")
max_num = max(lst2)
index_max = lst2.index(max_num)
print(f"Index of max num: {index_max}")
proizv = 1
for num in lst2:
    ed = num % 10
    if ed == 3:
        proizv *= num
if proizv == 1:
    print("There is no number with digit of units 3 !!!")
else:
    print(f"Multiplication: {proizv}")