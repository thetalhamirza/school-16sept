size = int(input("Enter triangle's size: "))

for i in range(1,size+1):
    for j in range(i):
        print('#',end='')
    print('')