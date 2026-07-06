# 🟠 Tip Calculator for Restaurants

A simple Python command-line tool that calculates per-person payment for a restaurant bill, including tip. Built as a beginner project to practice core Python fundamentals — variables, float operations, string formatting, and type conversion.

## What It Does

Takes three inputs from the user:
- **Bill amount** (total cost of the meal)
- **Tip percentage** (how much to tip, e.g. 15%, 20%)
- **Number of people** splitting the bill

It then calculates:
- Total tip amount
- Total bill including tip
- Amount each person owes

## Features

- ✅ Handles negative bill/tip input safely (clamped to non-negative)
- ✅ Handles zero or negative number of people (clamped to a minimum of 1)
- ✅ Currency-formatted output (`$xx.xx`)
- ✅ Colored terminal output using ANSI escape codes
- ✅ Supports decimal tip percentages (e.g. 17.5%)

## Concepts Practiced

- Multiple variables and data flow
- Float arithmetic
- `f-string` formatting vs string concatenation
- Type conversion (`int()`, `float()`, `abs()`, `max()`)
- ANSI terminal color codes

## How to Run

```bash
python tip_calculator.py
```

You'll be prompted to enter the bill amount, tip percentage, and number of people. The program will then print a formatted summary.

### Example

```
Enter the bill amount : 100
Enter tip percentage : 18
Enter num of people : 3

Tip Calculator
------------------
Bill Amount     : $100.00
Tip Percentage  : 18.0%
Number of People: 3
Tip Amount      : $18.00
Per Person Payment: $39.33
```

## Edge Case Handling

| Input | Behavior |
|---|---|
| Negative bill amount | Automatically converted to positive using `abs()` |
| Negative tip percentage | Automatically converted to positive using `abs()` |
| Zero or negative people | Automatically clamped to a minimum of `1` using `max()` |

> **Note:** This version handles edge cases without using `if` statements, loops, or functions — a constraint used intentionally to practice writing straight-line logic with built-in functions (`abs()`, `max()`). This means invalid input is *silently corrected* rather than rejected with an error message. A more robust version (using conditionals and input validation loops) is a natural next step.

## Project Structure

```
tip-calculator/
├── tip_calculator.py       # Main script
├── test_tip_calculator.py  # Test cases
└── README.md               # Project documentation
```

## Possible Improvements

- Add input validation with clear error messages (requires conditionals)
- Support splitting unevenly among people
- Add a GUI or web interface
- Round tip suggestions to common percentages (15%, 18%, 20%)

## License

Free to use and modify for learning purposes.