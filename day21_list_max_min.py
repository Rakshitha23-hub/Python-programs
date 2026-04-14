n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

max_val = lst[0]
min_val = lst[0]

for i in lst:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum:", max_val)
print("Minimum:", min_val)