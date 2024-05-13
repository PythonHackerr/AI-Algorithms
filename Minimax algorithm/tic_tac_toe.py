from enum import Enum
from minimax import minimax, check_win, best_move_min, best_move_max

class GameMode(Enum):
    Player_vs_Player = 1
    Player_vs_AI = 2
    AI_vs_AI = 3


def display_grid(grid):
    print()
    for row in grid:
        print(*row)
    print()




def init():
    global grid, game_mode, is_player_first, who_starts, depth1, depth2
    print("Enter the dimension of the grid")
    while True:
        try:
            N = int(input())
            if N < 2:
                print("Dimension must be greater that 1! Try again")
                continue
            else:
                break
        except:
                print("Try again")

    print("Pick game mode (1 - PvP / 2 - PvAI / 3-AIvAI)")
    while True:
        try:
            game_mode = GameMode(int(input()))
            break
        except:
            print("Must be between 1 and 3! Try again")
    
    if (game_mode == GameMode.Player_vs_AI):
        print("Pick difficulty for AI (depth)")
        while True:
            try:
                depth1 = int(input())
                if depth1 < 0:
                    print("Can't be negative! Try again")
                    continue
                else:
                    break
            except:
                print("Try again")
        depth2 = depth1

    if (game_mode == GameMode.AI_vs_AI):
        print("Pick difficulty for X AI (depth)")
        while True:
            try:
                depth1 = int(input())
                if depth1 < 0:
                    print("Can't be negative! Try again")
                    continue
                else:
                    break
            except:
                print("Try again")
        print("Pick difficulty for O AI (depth)")
        while True:
            try:
                depth2 = int(input())
                if depth2 < 0:
                    print("Can't be negative! Try again")
                    continue
                else:
                    break
            except:
                print("Try again")

    if (game_mode == GameMode.Player_vs_AI):
        print("Who starts first? (1-Player / 2-AI)")
        while True:
            try:
                is_player_first = int(input())
                if is_player_first != 1 and is_player_first != 2:
                    print("Must be 1 or 2! Try again")
                    continue
                else:
                    break
            except:
                print("Try again")
        is_player_first -= 1
    else:
        is_player_first = 0

    print("First player plays as X or O? ('X' / 'O')")
    while True:
        who_starts = input()
        if who_starts != 'X' and who_starts != 'O':
            print("Must be 'X' or 'O'! Try again")
            continue
        else:
            break
    
    grid = generate_grid(N)


def generate_grid(N):
    return [["-"] * N for _ in range(N)]


def play_game(grid, game_mode, is_player_first, who_starts, depth1, depth2, display_to_console=True):

    playing = True
    winner = None

    for turn in range(0,len(grid)**2):
        if (display_to_console):
            display_grid(grid)

        if (turn % 2 == (is_player_first)):
            if (game_mode == GameMode.Player_vs_AI or game_mode == GameMode.Player_vs_Player):
                print("Pick spot [row col]") 
                while True:
                    try:
                        row, col = map(int, input().split())
                        if (grid[row][col] != "-"):
                            print("Already occupied!")
                            continue
                        if (who_starts == "O" and is_player_first == 0 or who_starts == "X" and is_player_first == 1):
                            grid[row][col] = "O"
                        else:
                            grid[row][col] = "X"
                        break
                    except:
                        print("Try again!")
                        continue
            else:
                if (who_starts == "O" and is_player_first == 0 or who_starts == "X" and is_player_first == 1):
                    if (who_starts == "O" and is_player_first == 0):
                        result = best_move_max(grid, depth2)
                    else:
                        result = best_move_max(grid, depth1)
                    grid[result[0]][result[1]] = "O"
                else:
                    if (who_starts == "O" and is_player_first == 0):
                        result = best_move_min(grid, depth2)
                    else:
                        result = best_move_min(grid, depth1)
                    grid[result[0]][result[1]] = "X"
        else:
            if (game_mode == GameMode.Player_vs_Player):
                print("Pick spot [row col]") 
                while True:
                    try:
                        row, col = map(int, input().split())
                        if (grid[row][col] != "-"):
                            print("Already occupied!")
                            continue
                        if (who_starts == "O" and is_player_first == 0 or who_starts == "X" and is_player_first == 1):
                            grid[row][col] = "X"
                        else:
                            grid[row][col] = "O"
                        break
                    except:
                        print("Try again!")
                        continue
            else:
                if (who_starts == "O" and is_player_first == 0 or who_starts == "X" and is_player_first == 1):
                    if (who_starts == "O" and is_player_first == 0):
                        result = best_move_min(grid, depth1)
                    else:
                        result = best_move_min(grid, depth2)
                    grid[result[0]][result[1]] = "X"
                else:
                    if (who_starts == "O" and is_player_first == 0):
                        result = best_move_max(grid, depth1)
                    else:
                        result = best_move_max(grid, depth2)
                    grid[result[0]][result[1]] = "O"


        winner = check_win(grid)
        if winner != None:
            if (display_to_console):
                display_grid(grid)
            if (winner == "Tie"):
                print("Game over! It's a tie!")
            else:
                print(f"Game over! Player {winner} has won!")
            break

        if not playing:
            break

    if winner == None:
        print("Game over! It's a tie!")

    return winner


if __name__ == "__main__":
    init()
    print(play_game(grid, game_mode, is_player_first, who_starts, depth1, depth2))
