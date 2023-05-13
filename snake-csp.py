#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
def find_most_constrained_position(board):
    unassigned = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == '-']
    def count_adjacent_filled_cells(i, j):
        neighbors = [(i - 1, j),(i + 1, j),(i, j - 1),(i, j + 1)]
        return sum(1 for ni, nj in neighbors if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] != '-')
    row, col = max(unassigned, key=lambda ij: count_adjacent_filled_cells(*ij))
    return row, col

def is_valid_move(board, x, y, ch):
    neighbors = [(x - 1, y),(x + 1, y), (x, y - 1),(x, y + 1)]
    for nx, ny in neighbors:
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            neighbor = board[nx][ny]
            if abs(ord(neighbor) - ord(ch)) == 1:
                return True
    return False

def is_solution_valid(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if not is_valid_move(board, x, y, board[x][y]):
                return False
    return True

def solve_csp(board, available_letters, remaining_slots, filled_slots):
    if filled_slots == remaining_slots:
        return is_solution_valid(board)
    x, y = find_most_constrained_position(board)
    for ch in list(available_letters):
        if is_valid_move(board, x, y, ch):
            board[x][y] = ch
            available_letters.remove(ch)
            if solve_csp(board, available_letters, remaining_slots, filled_slots+1):
                return True 
            available_letters.add(ch)
            board[x][y] = '-'
    return False

def main():
    board = [['-', '-', '-', '-', 'Y'],['R', 'A', '-', '-', '-'],['-', '-', '-', '-', '-'],['-', 'E', '-', '-', '-'],['-', '-', '-', '-', 'K']]
    used_letters = set(cell for row in board for cell in row if cell != '-')
    remaining_slots = sum(1 for row in board for cell in row if cell == '-')
    filled_slots=0
    available_letters = set(string.ascii_uppercase[:-1])-used_letters
    if solve_csp(board, available_letters, remaining_slots,filled_slots):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end=" ")
            print()
    else:
        print("There is no solution")
   
if __name__ == "__main__":
    main()
