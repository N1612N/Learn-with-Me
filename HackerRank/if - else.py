n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0:
    if n > 20:
        print("Not Weird")
    elif n in range(1, 5+1):
        print("Not Weird")
    elif n in range(6, 20+1):
        print("Weird")
    else:
        print("Enter Valid Input")
else:
    print("Enter Valid Input")
