import random

dominoes = [[i, j] for i in range(7) for j in range(i, 7)]
random.shuffle(dominoes)
stock_pieces = dominoes[:14]
computer = dominoes[14:21]
player = dominoes[21:]

snake = max(max(computer), max(player))

if snake in computer:
    computer.remove(snake)
    status = 'player'
else:
    player.remove(snake)
    status = 'computer'

print("Stock pieces:", stock_pieces)
print("Computer pieces:", computer)
print("Player pieces:", player)
print("Domino snake:", [snake])
print("status:", status) 