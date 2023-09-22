#Q1

try:
    num = int(input("Enter a number: "))
    for i in range(1,11):
        print(num, "x", i, "=",end=' ')
        print(num*i)

except ValueError:
    print('plz enter number')




