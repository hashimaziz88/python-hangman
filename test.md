import argparse

def open_puzzle(file_name):
    puzzle = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        
        for line in lines:
    
            line = line.replace("\n", "")
            split_line = line.split(" ")
            puzzle.append(split_line)

    return puzzle

def write_to_file(solved_puzzle, solution_file):
    final_grid = []
    final_str = ""
    for line in range(len(solved_puzzle)):
        if line == len(solved_puzzle) - 1:
            final_grid.append(solved_puzzle[line])
        else:
            solved_puzzle[line].append("\n")
            final_grid.append(solved_puzzle[line])
    for line in final_grid:
        for char in line:
            if char == "\n":
                final_str += char

            else:
                final_str += char + " "
    final_str = final_str.strip()

    with open(solution_file, "w") as file:
        file.write(final_str)


def print_board(board):
    for row in range(9):
        for col in range(9):
            if col == 8:
                print(board[row][col])
            else:
                print(board[row][col], end=" | ")
        if row != 8:
            print("-" * 34)

def solve_sudoku(puzzle, path, solution_file):
    print(f"Solving puzzle from {path}")
    print_board(puzzle)

    write_to_file(puzzle, solution_file)

def main():
    parser = argparse.ArgumentParser(description="Puzzle to be solved by Sudoku solver.")
    parser.add_argument("puzzle_file", help="Path to the puzzle file")
    parser.add_argument("-o", "--overwrite")
    args = parser.parse_args()

    solution_file = args.overwrite
    puzzle_file = args.puzzle_file
    puzzle = open_puzzle(puzzle_file)
    solve_sudoku(puzzle, puzzle_file, solution_file)


if __name__ == "__main__":
    main()
