#!/usr/bin/python3
"""
N Queens Problem Solver

This script solves the N-Queens problem using an efficient backtracking algorithm.
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
        # Check row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on the left side
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
        # Base case: If all queens are placed, add solution
        if col >= N:
            solution = []
            for row in range(N):
                for c in range(N):
                    if board[row][c] == 1:
                        solution.append([row, c])
            solutions.append(solution)
            return
        
        # Try placing queen in each row of current column
        for row in range(N):
            if is_safe(board, row, col):
                # Place queen
                board[row][col] = 1
                
                # Recur to place queens in subsequent columns
                solve_util(board, col + 1, solutions)
                
                # Backtrack: remove queen to try next configuration
                board[row][col] = 0

    # Initialize board and solutions list
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    
    # Solve the problem
    solve_util(board, 0, solutions)
    return solutions


def main():
    """
    Main function to handle command-line arguments and solve N-Queens problem
    
    Time Complexity: O(N!)
    Space Complexity: O(N^2)
    """
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate N
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Additional validation
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve and print solutions
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()