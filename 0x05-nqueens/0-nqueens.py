#!/usr/bin/python3
"""
N Queens Problem Solver

This script solves the N-Queens problem using backtracking algorithm.
It finds all possible configurations of N queens on an N×N chessboard
where no two queens can attack each other.

Time Complexity: O(N!)
Space Complexity: O(N)
"""

import sys


def solve_nqueens(N):
    """
    Solve the N-Queens problem using backtracking.

    Args:
        N (int): Size of the chessboard and number of queens

    Returns:
        List of solutions, where each solution is a list of queen positions
    """
    def is_safe(board, row, col):
        """
        Check if a queen can be placed on board[row][col]

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_util(board, col, solutions):
        """
        Recursive utility function to solve N Queens using backtracking

        Time Complexity: O(N!)
        Space Complexity: O(N^2)
        """
        if col >= N:
            solution = []
            for row in range(N):
                for c in range(N):
                    if board[row][c] == 1:
                        solution.append([row, c])
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1

                solve_util(board, col + 1, solutions)

                board[row][col] = 0

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_util(board, 0, solutions)
    return solutions


def main():
    """
    Main function to handle command-line arguments and solve N-Queens problem

    Time Complexity: O(N!)
    Space Complexity: O(N^2)
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
