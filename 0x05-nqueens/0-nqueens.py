#!/usr/bin/python3
"""
N queens solution module.
This script solves the N-Queens problem using backtracking algorithm.
It finds all possible configurations of N queens on an NxN chessboard
where no two queens can attack each other.

Time Complexity: O(N!)
Space Complexity: O(N)
"""

import sys


def is_safe(board, row, col, n):
    """
    Checks if a queen can be placed on board[row][col].

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem and return all possible solutions.

    Time Complexity: O(N!)
    Space Complexity: O(N^2)
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve_util(board, col):
        """
        Recursive utility function to solve the N-Queens problem
        using backtracking.
        """
        if col >= n:
            solution = []
            for row in range(n):
                for c in range(n):
                    if board[row][c] == 1:
                        solution.append([row, c])
            solutions.append(solution)
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve_util(board, col + 1)
                board[row][col] = 0
    solve_util(board, 0)
    return solutions


def get_input():
    """
    Main function to handle command-line arguments and solve N-Queens problem

    Time Complexity: O(N!)
    Space Complexity: O(N^2)
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
