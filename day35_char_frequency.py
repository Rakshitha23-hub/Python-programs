s = input("Enter a string: ")

visited = []

for ch in s:
    if ch not in visited:
        count = 0
        for c in s:
            if ch == c:
                count += 1
        print(ch, "occurs", count, "times")
        visited.append(ch)