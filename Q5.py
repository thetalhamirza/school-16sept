press = int(input("Enter number of fishes: "))
height = int(input("Enter fish's height: "))

for i in range(press):

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

    track = track - 2
    cut = 1
    while track != 1:
        track = track - 2
        for spaced in range(cut):
            print(" ", end='')
        for tagout in range(track):
            print("#", end='')
        print()
        cut = cut + 1

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
