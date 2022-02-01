import random
# pulls n random pieces from the domino set
def get_domino_pieces(n):
    domino_pieces = []
    for _ in range(n):
        rn = random.randint(0, len(domino_set) - 1)
        domino_pieces.append(domino_set[rn])
        del domino_set[rn]
    return domino_pieces
# returns max double piece in domino set
def max_double(pieces_list):
    doubles_list = [piece for piece in pieces_list if piece[0] == piece[1]]
    if doubles_list:
        return max(doubles_list)
    else:
        return []
# returns current status message
def message(st):
    return {
        'computer': '\nStatus: Computer is about to make a move. Press Enter to continue...',
        'player': '\nStatus: It\'s your turn to make a move. Enter your command.',
        'player_win': '\nStatus: The game is over. You won!',
        'computer_win': '\nStatus: The game is over. The computer won!',
        'draw': '\nStatus: The game is over. It\'s a draw!'
        }[st]
# prints current playing field
def current_stage(stat):
    print('=' * 70)
    print('Stock size:', len(domino_set))
    print('Computer pieces:', str(len(computer_pieces)) + '\n')
    if len(domino_snake) <= 6:
        print("".join(domino_snake) + '\n')
    else:
        print("".join(domino_snake[:3]) + '...' + "".join(domino_snake[-3:]) + '\n')
    print('Your pieces:')
    for i in range(len(player_pieces)):
        print(str(i + 1) + ':' + str(player_pieces[i]))
    print(message(stat))
# makes one move
def make_a_move(m, pieces):
    if m > 0:
        domino = pieces[m - 1]
        right_snake = int(domino_snake[-1][4])
        if domino.count(right_snake) > 0:
            if right_snake == domino[1]:
                domino = [domino[1], domino[0]]
            domino_snake.append(str(domino))
            del pieces[m - 1]
        else:
            return 'Illegal'
    if m < 0:
        domino = pieces[-m - 1]
        left_snake = int(domino_snake[0][1])
        if left_snake in domino:
            if left_snake == domino[0]:
                domino = [domino[1], domino[0]]
            domino_snake.insert(0, str(domino))
            del pieces[-m - 1]
        else:
            return 'Illegal'
    if m == 0:
        if domino_set:
            pieces.extend(get_domino_pieces(1))
# sets first domino
while True:
    # generates full domino set
    domino_set = [[a, b] for a in range(7) for b in range(7) if a <= b]
    computer_pieces = get_domino_pieces(7)
    player_pieces = get_domino_pieces(7)
    first_domino = max(max_double(computer_pieces), max_double(player_pieces))
    if first_domino:
        break
domino_snake = []
if first_domino in player_pieces:
    player_pieces.remove(first_domino)
    status = 'computer'
else:
    computer_pieces.remove(first_domino)
    status = 'player'
domino_snake.append(str(first_domino))
# play: take turns until the end of the game
while True:
    current_stage(status)
    if status in ['player_win', 'computer_win', 'draw']:
        break
    if status == 'player':
        while True:
            try:
                move = int(input())
            except ValueError:
                print('Invalid input. Please try again.')
                continue
            if int(move) not in range(-len(player_pieces), len(player_pieces) + 1):
                print('Invalid input. Please try again.')
                continue
            if make_a_move(int(move), player_pieces) == 'Illegal':
                print('Illegal move. Please try again.')
                continue
            break
        status = 'computer'
    elif status == 'computer':
        enter = input()
        while True:
            move = random.randint(-len(computer_pieces), len(computer_pieces))
            if make_a_move(move, computer_pieces) == 'Illegal':
                continue
            break
        status = 'player'
    if domino_snake[0][1] == domino_snake[-1][4] and "".join(domino_snake).count(domino_snake[0][1]) == 8:
        status = 'draw'
    if len(player_pieces) == 0:
        status = 'player_win'
    if len(computer_pieces) == 0:
        status = 'computer_win'


