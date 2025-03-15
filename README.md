# Student Progression Outcome Predictor

## Overview
This project is a Python program designed to predict student progression outcomes based on university regulations. The program evaluates student credit allocations and determines whether they progress, trail, retrieve modules, or are excluded.

## Features
- **User Input Validation**: Ensures only valid integer inputs (0, 20, 40, 60, 80, 100, 120) are accepted.
- **Progression Outcome Calculation**: Determines the progression category based on credit distribution.
- **Multiple Student Processing**: Allows multiple student entries in a loop until the user quits.
- **Histogram Visualization**: Uses `graphics.py` to display a histogram of progression outcomes.
- **Data Storage**:
  - **List Implementation**: Stores and displays progression data from a list.
  - **Text File Storage**: Saves inputted progression data to a text file for later retrieval.

## How It Works
1. The user enters the number of credits at **Pass**, **Defer**, and **Fail**.
2. The program validates the input:
   - Ensures values are integers.
   - Checks if credits are within the allowed range.
   - Ensures the total of Pass, Defer, and Fail equals 120.
3. The appropriate progression outcome is displayed.
4. Users can continue entering data or quit to display results.
5. When quitting, a histogram of results is generated.
6. Stored data is printed from a list (Part 2) and a text file (Part 3).

## Example Run
```
Enter your total PASS credits: 100
Enter your total DEFER credits: 20
Enter your total FAIL credits: 0
Progress (module trailer)
Would you like to enter another set of data? (y/q): y
Enter your total PASS credits: 60
Enter your total DEFER credits: 0
Enter your total FAIL credits: 60
Module retriever
Would you like to enter another set of data? (y/q): q

Histogram:
Progress: |||
Module retriever: ||

Stored Data (Part 2 & 3):
Progress - 120, 0, 0
Progress (module trailer) - 100, 0, 20
Module retriever - 80, 20, 20
Exclude - 40, 0, 80
```

## Technologies Used
- **Python** (Core logic and validation)
- **graphics.py** (Histogram visualization)
- **File Handling** (Saving and retrieving data)


