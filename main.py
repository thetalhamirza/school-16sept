num = int(input("enter lucky numver: "))

if num % 10 == 0:
    print("Divisible by 10")
    print("Even")
else:
    print("Not divisible")
    if num % 2 == 0:
        print("Even")
    else:
        print('odd')
