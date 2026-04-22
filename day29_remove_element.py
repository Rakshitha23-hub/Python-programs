n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

key = int(input("Enter element to remove: "))

result = []

for i in lst:
    if i != key:
        result.append(i)

print("Updated list:", result)