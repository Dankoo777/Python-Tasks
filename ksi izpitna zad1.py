lst = []
while True:
    try:
        n = int(input("Input n: "))
    except ValueError:
        print("Not Int!")
        continue
    if n > 15 and n < 35:
        break
    else:
        print("Must be between 15 and 35")
        continue
for i in range(n):
    while True:
        try:
            num = int(input("Input num: "))
        except ValueError:
            print("Not Int!")
            continue
        if num >= 30 and n <= 300:
            break
        else:
            print("Must be between 30 and 300")
            continue
    lst.append(num)
print(f"List 1: {lst}")
count = 0
for num in lst:
    des = (num // 10) % 10
    if des % 3 == 0:
        count += 1
print(f"Count of elements with des % 3 == 0 is: {count}")
lst_copy = lst.copy()
lst_copy.sort()
needed_num = 0
for i in lst_copy:
    if i % 6 == 4:
        needed_num = i
        break
index = lst.index(needed_num)
print(f"Index of the min (num % 6 == 4) is: {index}")
lst2 = [num for num in lst if ((num % 2 == 0 or num % 3 == 0) and (num > 9 and num < 100))]
print(f"List 2: {lst2}")
suma = 0
new_count = 0
for index1 in range(len(lst2)):
    if index1 % 2 == 1:
        suma += lst2[index1]
        new_count += 1
sr_aritm = suma / new_count
print(f"Sredno aritmetichno: {sr_aritm}")
lst3 = [num for num in lst2 if num % 2 == 0]
min_chet = min(lst3)
lst2.remove(min_chet)
print(f"New list2: {lst2}")

