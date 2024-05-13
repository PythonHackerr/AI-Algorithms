import math
import random

scores = {
    "X" : 1,
    "O" : -1,
    "Tie": 0
}


def check_horizontals(grid):
    for row in range(len(grid)):
        first_element = grid[row][0]
        if (first_element == "-"):
            continue
        won = True
        for col in range(len(grid)):
            if grid[row][col] != first_element:
                won = False
        if won:
            return first_element
    return None


def check_verticals(grid):
    for col in range(len(grid)):
        first_element = grid[0][col]
        if (first_element == "-"):
            continue
        won = True
        for row in range(len(grid)):
            if grid[row][col] != first_element:
                won = False
        if won:
            return first_element
    return None


def check_diagonals(grid):
    first_element = grid[0][0]
    if (first_element != "-"):
        won = True
        for i in range(len(grid)):
            if grid[i][i] != first_element:
                won = False
                break
        if won:
            return first_element

    first_element = grid[0][len(grid)-1]
    if (first_element != "-"):
        won = True
        for i in range(1, len(grid)+1):
            if grid[i-1][len(grid)-i] != first_element:
                won = False
                break
        if won:
            return first_element
    return None


def empty_spots(grid):
    spots = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[col][row] == "-":
                spots += 1
    return spots


def check_win(grid):
    horizontals = check_horizontals(grid)
    verticals = check_verticals(grid)
    diagonals = check_diagonals(grid)

    if (horizontals != None):
        return horizontals
    if (verticals != None):
        return verticals
    if (diagonals != None):
        return diagonals

    if (empty_spots(grid) == 0):
        return "Tie"
    return None



def minimax(grid, depth, is_max, n, alpha = -math.inf, beta = math.inf):
    winner = check_win(grid)
    if winner:
        return scores[winner]
    if (depth == 0):
        return 0

    if is_max:
        best_score = -math.inf
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "-":
                    grid[i][j] = "X"
                    score = minimax(grid, depth-1, False, n, alpha, beta)
                    grid[i][j] = "-"
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta > alpha:
                        pass
        return best_score
    else:
        best_score = math.inf
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "-":
                    grid[i][j] = "O"
                    score = minimax(grid, depth-1, True,n, alpha, beta)
                    grid[i][j] = "-"
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if alpha > beta:
                        pass
        return best_score


def best_move_min(grid, depth):
    n = len(grid)
    best_score = -math.inf
    best_moves = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "-":
                grid[i][j] = "X"
                score = minimax(grid, depth, False, len(grid))
                grid[i][j] = "-"
                if score > best_score:
                    best_score = score
                    best_moves.clear()
                    best_moves.append((i, j))
                elif score == best_score:
                    best_moves.append((i, j))
    print(f"best_moves for min player (X) : {best_moves}")
    move = random.choice(best_moves)
    return move


def best_move_max(grid, depth):
    best_score = math.inf
    best_moves = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "-":
                grid[i][j] = "O"
                score = minimax(grid, depth, True, len(grid))
                grid[i][j] = "-"
                if score < best_score:
                    best_score = score
                    best_moves.clear()
                    best_moves.append((i, j))
                elif score == best_score:
                    best_moves.append((i, j))
    print(f"best_moves for max player (O) : {best_moves}")
    move = random.choice(best_moves)
    return move