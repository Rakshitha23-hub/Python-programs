s = input("Enter a sentence: ")

count = 0

for ch in s:
    if ch == " ":
        count += 1

print("Number of words:", count + 1)