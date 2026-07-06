# BMI Calculator

A simple Python command-line tool that calculates Body Mass Index (BMI) from user-provided weight and height, then classifies the result into a standard health category.

---

## What is BMI?

**Body Mass Index (BMI)** is a numerical value derived from a person's weight and height. It's a widely used screening tool to categorize body weight into ranges that may indicate whether a person is underweight, at a normal weight, overweight, or obese.

> ⚠️ **Note:** BMI is a general screening tool, not a diagnostic measure. It doesn't account for muscle mass, bone density, body composition, or distribution of fat. Always consult a healthcare professional for a full health assessment.

---

## Formula

```
BMI = weight (kg) / height (m)²
```

Where:
- **weight** is measured in kilograms (kg)
- **height** is measured in meters (m)
- The result is expressed in kg/m²

### Example

For a person weighing **70 kg** with a height of **1.75 m**:

```
BMI = 70 / (1.75 × 1.75)
BMI = 70 / 3.0625
BMI = 22.86 kg/m²
```

---

## BMI Categories

| BMI Range         | Category       |
|--------------------|---------------|
| Below 18.5          | Underweight    |
| 18.5 – 24.9         | Normal weight  |
| 25.0 – 29.9         | Overweight     |
| 30.0 and above      | Obese          |

*(Based on the standard WHO BMI classification for adults.)*

---

## How to Run

### Requirements
- Python 3.x

### Steps

1. Clone or download this repository.
2. Run the script:

```bash
python bmi_calculator.py
```

3. Enter your weight (in kg) and height (in meters) when prompted.

### Sample Run

```
Enter weight in kgs : 70
Enter height in mtrs : 1.75
BMI Calculator
------------------
BMI       : 22.86 kg/m^2
Category  : Normal
```

---

## Key Concepts Practiced

- Float arithmetic
- Type conversion (`float()`)
- String formatting (f-strings, `.2f` decimal precision)
- Value classification using `bisect` (range-based lookup) instead of conditional statements

---

## Project Structure

```
bmi_calculator/
├── bmi_calculator.py
└── README.md
```

---

## Possible Improvements

- Add input validation for zero, negative, or non-numeric values
- Support both metric and imperial units (kg/lbs, m/ft-in)
- Add unit tests for the BMI calculation and categorization logic
- Build a simple GUI or web interface

---

## License

This project is open-source and available for educational use.