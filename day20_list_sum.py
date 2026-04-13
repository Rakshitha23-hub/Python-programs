n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

total = 0
for i in lst:
    total += i

print("Sum of elements:", total)