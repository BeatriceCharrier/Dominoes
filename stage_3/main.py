import random

full_domino_set = [[i, j] for i in range(7) for j in range(i, 7)]
snakes = [x for x in full_domino_set if x[0] == x[1]]
stock_pieces = []
computer_pieces = []
player_pieces = []
game_snake = []
status = ''
game_in_play = True


def check_game_win():
    global game_in_play
    if len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        game_in_play = False
    elif len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        game_in_play = False
    elif is_draw(game_snake):
        print("Status: The game is over. It's a draw!")
        game_in_play = False


def deal_dominoes():
    current_set_of_dominoes = full_domino_set[:]
    stock_pieces.clear()
    computer_pieces.clear()
    player_pieces.clear()
    game_snake.clear()
    while current_set_of_dominoes:
        stock_pieces.append(current_set_of_dominoes.pop((random.randint(0, len(current_set_of_dominoes)-1))))
        computer_pieces.append(current_set_of_dominoes.pop(random.randint(0, len(current_set_of_dominoes)-1)))
        player_pieces.append(current_set_of_dominoes.pop(random.randint(0, len(current_set_of_dominoes)-1)))
        stock_pieces.append(current_set_of_dominoes.pop(random.randint(0, len(current_set_of_dominoes)-1)))


def first_play():
    global status
    status = ""
    for snake_piece in snakes[-1:0:-1]:
        if snake_piece in computer_pieces:
            game_snake.append(snake_piece)
            computer_pieces.remove(snake_piece)
            status = "player"
            return
        elif snake_piece in player_pieces:
            game_snake.append(snake_piece)
            player_pieces.remove(snake_piece)
            status = "computer"
            return
        else:
            continue


def is_draw(dominoes):
    flattened_dominoes = ""
    for domino in dominoes:
        flattened_dominoes += f'{domino[0]}{domino[1]}'
    if flattened_dominoes[0] == flattened_dominoes[-1]:
        if flattened_dominoes.count(flattened_dominoes[0]) == 8:
            return True


def play_game():
    global status
    print_game()
    check_game_win()
    if not game_in_play:
        return
    if status == 'computer':
        print(f"Status: Computer is about to make a move. Press Enter to continue...")
        play = random.randint(len(computer_pieces)*-1, len(computer_pieces))
        play_piece(play, computer_pieces)
        status = "player"
        input()
    else:
        while True:
            play = input("Status: It's your turn to make a move. Enter your command.")
            try:
                play = int(play)
                if len(player_pieces)*-1 > play or len(player_pieces) < play:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid input. Please try again.")

        play_piece(play, player_pieces)
        status = "computer"


def play_piece(play, var):
    if play > 0:
        play -= 1
        game_snake.append(var[play])
        del var[play]
    elif play < 0:
        play = play * -1 - 1
        game_snake.insert(0, var[play])
        del var[play]
    else:
        var.append(stock_pieces.pop())


def print_game():
    print('=' * 70)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}\n")
    if len(game_snake) > 6:
        print(f'{game_snake[0]}{game_snake[1]}{game_snake[2]}...{game_snake[-3]}{game_snake[-2]}{game_snake[-1]}\n')
    else:
        return_string = ""
        for domino in game_snake:
            return_string += f'{domino}'
        print(f'{return_string}\n')
    print(f'Player pieces: ')
    count = 0
    for domino in player_pieces:
        count += 1
        print(f'{count}:{domino}')
    print()


if __name__ == '__main__':
    deal_dominoes()
    first_play()
    while game_in_play:
        play_game()

