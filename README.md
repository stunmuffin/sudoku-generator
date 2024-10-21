# Sudoku Puzzle Generator with Solution

This project generates and solves Sudoku puzzles. It can generate puzzles of varying difficulty levels (easy, medium, hard) and save them as both images (PNG format) and CSV files.

## Features

- Generates valid 9x9 Sudoku puzzles.
- Allows choosing difficulty levels: easy, medium, and hard.
- Saves generated Sudoku puzzles as PNG images.
- Optionally shows solutions for the puzzles in the saved images.
- Exports puzzles and their solutions as CSV files.

## Requirements

You can install the required packages using the following:

```bash
pip install -r requirements.txt
```

Sudoku example:

![sudoku_easy_1](https://github.com/user-attachments/assets/8be9c8cc-7c66-4ded-866f-34df03a6604a)


Sudoku result:

![sudoku_easy_result1](https://github.com/user-attachments/assets/6412ca6f-ee2c-4c60-a5fc-43225fd9ad44)

## Functions

create_sudoku(base=3): Generates a valid Sudoku puzzle. By default, it creates a 9x9 grid.

remove_numbers(sudoku, difficulty): Removes numbers from the puzzle to create a challenge. The difficulty can be:

- 'easy': 25% of cells are removed.
- 'medium': 50% of cells are removed.
- 'hard': 75% of cells are removed.

save_sudoku_as_png(sudoku, filename, show_solution=False, solution=None): Saves the current state of the Sudoku puzzle as a PNG image. If show_solution=True, it highlights the solution in red.

save_sudoku_to_csv(sudoku, filename): Saves the Sudoku puzzle to a CSV file.

## How to Use

1.) Set Difficulty Level: 

Inside the main() function, adjust the difficulty level by changing the difficulty_level variable. The available options are:

- 'easy'
- 'medium'
- 'hard'

example: 

```bash
difficulty_level = 'easy'
```
2.) Set the Number of Puzzles: 

Adjust the number of Sudoku puzzles to generate by modifying the number_of_puzzles variable. 

Example:

```bash
number_of_puzzles = 1
```

3.) Run the Script: 

After adjusting the parameters, you can run the script using Python:

```bash
python sudoku_generator.py
```

The script will generate the puzzle(s), remove numbers according to the difficulty level, and save the outputs as PNG images and CSV files.

Output Files

For each Sudoku puzzle generated, the following files are created:

- Sudoku Image: PNG image of the incomplete Sudoku puzzle (e.g., sudoku_easy_1.png).

- Solution Image: PNG image of the Sudoku puzzle with the solution highlighted in red (e.g., sudoku_easy_result1.png).

- Sudoku Puzzles CSV: A CSV file containing the incomplete puzzles (e.g., sudoku_puzzles.csv).

- Sudoku Solutions CSV: A CSV file containing the solutions (e.g., sudoku_solutions.csv).







