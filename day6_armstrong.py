n=int(input("Enter a number:"))
original=n
total=0
while n!=0:
    digit=n%10
    total=total+(digit*digit*digit)
    n=n//10
if original==total:
    print("Armstrong")
else:
    print("Not Armstrong")