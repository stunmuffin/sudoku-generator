import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd  # Library added for CSV handling

def create_sudoku(base=3):
    """Create a valid Sudoku puzzle (3x3 = 9x9 size)."""
    side = base * base
    sudoku = np.zeros((side, side), dtype=int)

    def is_valid(row, col, num):
        """Check if the given number can be placed."""
        if num in sudoku[row] or num in sudoku[:, col]:
            return False
        start_row = row - row % base
        start_col = col - col % base
        if num in sudoku[start_row:start_row + base, start_col:start_col + base]:
            return False
        return True

    def fill(row, col):
        """Function to fill the Sudoku."""
        if row == side:  # If all rows are filled
            return True
        if col == side:  # A row is filled, move to the next row
            return fill(row + 1, 0)

        if sudoku[row][col] != 0:  # If the cell is already filled, move to the next cell
            return fill(row, col + 1)

        numbers = list(range(1, base * base + 1))
        random.shuffle(numbers)  # Shuffle the numbers
        for num in numbers:
            if is_valid(row, col, num):
                sudoku[row][col] = num  # Place the number
                if fill(row, col + 1):  # Move to the next cell
                    return True
                sudoku[row][col] = 0  # Backtrack

        return False

    fill(0, 0)  # Start filling from the first cell
    return sudoku

def remove_numbers(sudoku, difficulty):
    """Remove numbers from the Sudoku matrix based on the difficulty level."""
    base = 3
    side = base * base

    # Determine the number of empty cells based on difficulty level
    if difficulty == 'easy':
        num_to_remove = side ** 2 // 4  # 25% empty
    elif difficulty == 'medium':
        num_to_remove = side ** 2 // 2  # 50% empty
    elif difficulty == 'hard':
        num_to_remove = (side ** 2 * 3) // 4  # 75% empty
    else:
        num_to_remove = side ** 2 // 2  # Default: medium

    # Remove the numbers
    count = 0
    while count < num_to_remove:
        x = random.randint(0, side - 1)
        y = random.randint(0, side - 1)
        if sudoku[x][y] != 0:  # If not already empty
            sudoku[x][y] = 0  # Make empty
            count += 1

def save_sudoku_as_png(sudoku, filename='sudoku.png', show_solution=False, solution=None):
    """Save the Sudoku matrix as a PNG image."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.matshow(np.ones_like(sudoku) * -1, cmap='Blues', alpha=0.01)  # Background color
    for (i, j), val in np.ndenumerate(sudoku):
        ax.text(j, i, f'{int(val)}' if val != 0 else '', ha='center', va='center', fontsize=18)

    if show_solution and solution is not None:
        # Display the solution by filling only the empty cells
        for (i, j), val in np.ndenumerate(sudoku):
            if val == 0:  # If the cell is empty
                correct_value = solution[i][j]
                ax.text(j, i, f'{int(correct_value)}', ha='center', va='center', fontsize=18, color='red')

    # Add grid
    ax.set_xticks(np.arange(-0.5, sudoku.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, sudoku.shape[0], 1), minor=True)
    ax.grid(which='minor', color='lightgray', linewidth=0.5)  # Light grid color and thickness

    # Main grid lines
    for i in range(0, sudoku.shape[0] + 1):
        if i % 3 == 0:  # Thick lines every 3 cells
            ax.axhline(i - 0.5, color='black', linewidth=2)
            ax.axvline(i - 0.5, color='black', linewidth=2)
        else:  # Thin lines for other cells
            ax.axhline(i - 0.5, color='lightgray', linewidth=0.5)
            ax.axvline(i - 0.5, color='lightgray', linewidth=0.5)

    ax.set_xticks([])  # Remove numbers on the X axis
    ax.set_yticks([])  # Remove numbers on the Y axis
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
    print(f"Sudoku image saved as '{filename}'.")

def save_sudoku_to_csv(sudoku, filename):
    """Save the Sudoku matrix in CSV format."""
    df = pd.DataFrame(sudoku)
    df.to_csv(filename, index=False, header=False)
    print(f"Sudoku data saved as '{filename}'.")

def main():
    # Get difficulty level and number of puzzles from user
    difficulty_level = 'easy'  # Choose from 'easy', 'medium', or 'hard'
    number_of_puzzles = 1  # Number of Sudokus to generate

    puzzles = []  # Sudoku puzzles
    solutions = []  # Sudoku solutions

    for i in range(number_of_puzzles):
        sudoku = create_sudoku(base=3)  # 3x3 base (9x9 Sudoku)
        solution = sudoku.copy()  # Solved Sudoku
        remove_numbers(sudoku, difficulty_level)
        save_sudoku_as_png(sudoku, filename=f'sudoku_{difficulty_level}_{i + 1}.png')
        
        # Save solved Sudoku, filling only the empty cells
        save_sudoku_as_png(sudoku, filename=f'sudoku_{difficulty_level}_result{i + 1}.png', show_solution=True, solution=solution)

        # Save Sudokus and solutions
        puzzles.append(sudoku.flatten())  # Save flattened version
        solutions.append(solution.flatten())  # Save flattened version

    # Save to CSV files
    puzzles_df = pd.DataFrame(puzzles)
    solutions_df = pd.DataFrame(solutions)

    # Save Sudoku puzzles to CSV
    puzzles_df.to_csv('sudoku_puzzles.csv', index=False, header=False)
    # Save Sudoku solutions to CSV
    solutions_df.to_csv('sudoku_solutions.csv', index=False, header=False)

    print(f"{number_of_puzzles} {difficulty_level} level Sudoku puzzles were created, saved, and exported to CSV.")

if __name__ == "__main__":
    main()
