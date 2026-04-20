n1 = int(input("Enter number of elements in list 1: "))
list1 = []

for i in range(n1):
    num = int(input("Enter element: "))
    list1.append(num)

n2 = int(input("Enter number of elements in list 2: "))
list2 = []

for i in range(n2):
    num = int(input("Enter element: "))
    list2.append(num)

merged = []

for i in list1:
    merged.append(i)

for i in list2:
    merged.append(i)

print("Merged list:", merged)