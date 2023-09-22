print('Rock, Paper, Scissors!')

trials = int(input("Best of how many rounds? --> "))
p1score = 0
p2score = 0

p1 = input('Player 1, enter your name: ')
print(f"Hi, {p1}")
p2 = input('Player 2, enter your name: ')
print(f"Hi, {p2}")
print()
print('Remember to enter the choices with correct spelling and small-case')
print()

for i in range(trials):
    p1choice = input(f"{p1}, please enter either 'rock', 'paper', or 'scissors': ")
    p2choice = input(f"{p2}, please enter either 'rock', 'paper', or 'scissors': ")

    if p1choice == 'rock':
        if p2choice == 'rock':
            print('draw')
        elif p2choice == 'paper':
            print(f'{p2} wins this round!')
            p2score = p2score + 1
        elif p2choice == 'scissors':
            print(f'{p1} wins this round!')
            p1score = p1score + 1
    elif p1choice == 'paper':
        if p2choice == 'rock':
            print(f'{p1} wins this round!')
            p1score = p1score + 1
        elif p2choice == 'paper':
            print('draw')
        elif p2choice == 'scissors':
            print(f'{p2} wins this round!')
            p2score = p2score + 1
    elif p1choice == 'scissors':
        if p2choice == 'rock':
            print(f'{p2} wins this round!')
            p2score = p2score + 1
        elif p2choice == 'paper':
            print(f'{p1} wins this round!')
            p1score = p1score + 1
        elif p2choice == 'scissors':
            print('draw')

if p1score > p2score:
    print(f'{p1} wins the game!')
elif p1score < p2score:
    print(f'{p2} wins the game!')
else:
    print("The game is a draw")