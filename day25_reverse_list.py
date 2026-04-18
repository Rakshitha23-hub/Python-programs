n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

rev = []

for i in range(n - 1, -1, -1):
    rev.append(lst[i])

print("Reversed list:", rev)