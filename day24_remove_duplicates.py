n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print("List without duplicates:", unique)