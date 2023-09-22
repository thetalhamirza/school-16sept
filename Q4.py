height = int(input("Enter pyramid's height: "))

num = height
track = 1
for line in range(1,height+1):

    for space in range(num-1):
        print(' ',end='')
    num = num - 1

    for tag in range(track):
        print("#",end='')
    track = track + 2
    print('')