try:
    num = int(input("Enter number of apples : "))
    minim = int(input("Enter the minimum range : "))
    maxim = int(input("Enter the maximum range : "))
except ValueError:
    print("Please Enter integers only")
    quit()

if num < maxim or num < minim:
    print("Range should not be greater than apples")
    quit()

if minim == maxim:
    print("this is not a range")
    if num % minim == 0:
        print(f"{minim} is divisor of {num}")
    else:
        print(f"{minim} is not a divisor of {num}")

elif maxim < minim:
    for i in range(maxim, minim+1):
        if num % i == 0:
            print(f"{i} is divisor of {num}")
        else:
            print(f"{i} is not a divisor of {num}")

else:
    for i in range(minim, maxim+1):
        if num % i == 0:
            print(f"{i} is divisor of {num}")
        else:
            print(f"{i} is not a divisor of {num}")
