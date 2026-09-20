x = int(input("Enter a number: "))
if x % 2 == 0:
    print("The number is even.")
    if x > 10:
        print("Greater than 10")
    else:
        print("Less than 10")
else:
    print("The number is odd.")
