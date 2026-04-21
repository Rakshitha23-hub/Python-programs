n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

visited = []

for i in lst:
    if i not in visited:
        count = 0
        for j in lst:
            if i == j:
                count += 1
        print(i, "occurs", count, "times")
        visited.append(i)