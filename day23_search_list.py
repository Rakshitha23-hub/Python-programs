n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

key = int(input("Enter element to search: "))

found = False

for i in lst:
    if i == key:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")