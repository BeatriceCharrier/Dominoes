import random
dominoes = [[i, j] for i in range(7) for j in range(i, 7)]
random.shuffle(dominoes)
stock = dominoes[:14]
computer = dominoes[14:21]
player = dominoes[21:]

snake = max(max(computer), max(player))

if snake in computer:
    computer.remove(snake)
    status = 'player'
else:
    player.remove(snake)
    status = 'computer'

print('=' * 70)
print("Stock size:", len(stock))
print("Computer pieces:", len(computer))
print()
print(snake)
print()
print("Your pieces:")
for i in range(len(player)):
    n = i + 1
    pieces = player[i]
    print("{}:{}".format(n,pieces))

if status == 'player':
    print()
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print()
    print("Status: Computer is about to make a move. Press Enter to continue...")




