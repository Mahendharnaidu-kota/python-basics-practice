# Simple Math Quiz

A beginner Python project that asks 3 math questions, checks the user's answers, and prints a final score with percentage and feedback — **without using loops, conditionals, or functions**. This constraint makes it a great exercise for understanding how Python handles input/output and expressions under the hood.

## What It Does

1. Prints a math question
2. Reads the user's answer via `input()`
3. Compares it to the correct answer
4. Repeats for 3 questions
5. Prints the total score, percentage, and feedback for each question

## Example Output

```
Question 1: What is 5 + 2?
Enter answer 1: 7
Great job!
----------------------------------------
Question 2: What is 4 divided by 2?
Enter answer 2: 2
Great job!
----------------------------------------
Question 3: What is 10 squared (10^2)?
Enter answer 3: 99
Try again!
----------------------------------------
You got 2/3 correct (66.67%)
```

## Key I/O Concepts Practiced

### 1. `input()` returns a string
Every call to `input()` returns text (`str`), even if the user types numbers. That's why we wrap it:

```python
ans1 = float(input("Enter answer 1: "))
```

`input()` collects the raw text, and `float()` converts ("casts") it into a number so it can be compared and used in math. If you skip the `float()` conversion, `"7" == 7` would be `False`, because a string is never equal to a number in Python, even if they "look" the same.

### 2. Comparison expressions produce booleans
```python
is_correct1 = (ans1 == 7)
```

The `==` operator doesn't run a branch — it **evaluates to a value**: `True` or `False`. That value is a full-fledged Python object (of type `bool`) and can be stored in a variable, printed, or used in arithmetic, just like any other value.

### 3. `bool` is secretly an `int`
In Python, `True` behaves exactly like `1`, and `False` behaves exactly like `0`. This lets us total up correct answers without writing `if` statements:

```python
score = is_correct1 + is_correct2 + is_correct3
```

If two out of three answers are correct, this evaluates to `1 + 0 + 1 = 2`.

### 4. Boolean indexing instead of `if` / `else`
Normally, choosing between two messages ("Great job!" vs "Try again!") is written with `if`/`else`. Since this project intentionally avoids conditionals, we use the fact that `True`/`False` act as `1`/`0` to **index directly into a list**:

```python
feedback1 = ["Try again!", "Great job!"][is_correct1]
```

- If `is_correct1` is `False` (`0`) → picks index `0` → `"Try again!"`
- If `is_correct1` is `True` (`1`) → picks index `1` → `"Great job!"`

This is a neat trick for learning, but in real production code, an `if`/`else` or ternary expression (`"Great job!" if is_correct1 else "Try again!"`) is usually preferred for readability. This project avoids both on purpose, as a constraint-driven exercise.

### 5. Formatted output with f-strings
```python
print(f"You got {score}/{total} correct ({percentage:.2f}%)")
```

An f-string lets you embed variables and expressions directly inside a string using `{}`. The `:.2f` format spec rounds a float to exactly 2 decimal places, which is why `66.666...` becomes `66.67`.

### 6. Calculating percentage
```python
percentage = (score / total) * 100
```

Dividing an `int` by an `int` in Python 3 always produces a `float` (true division), so `2 / 3` gives `0.6666...`, not `0`. Multiplying by `100` converts that fraction into a percentage.

## Constraints Practiced

This version deliberately avoids:
- **Loops** (`for`, `while`) — each question is written out individually instead of repeated in a loop
- **Conditionals** (`if`, `else`, ternary expressions) — feedback is chosen via list indexing on a boolean instead
- **Functions** (`def`) — there's no reusable function; all logic runs top-to-bottom in the main script

This is a good way to see how much can be done using pure **expressions** and **data structures** (lists, booleans, arithmetic) before reaching for control-flow statements.

## Known Limitations

- **No input validation.** If the user types a non-numeric answer (like `"seven"`), `float()` raises a `ValueError` and the program crashes. Handling this gracefully normally requires a `try`/`except` block, which is a control-flow construct and was intentionally left out here.
- **Strict equality on floats.** Answers are compared with `==`, which works fine for the exact values in this quiz, but comparing floating-point numbers with `==` can be unreliable in general (e.g. results of division or repeated arithmetic). A more robust approach uses a small tolerance, like `abs(a - b) < 1e-9`.

## Next Steps (Ideas for Extending)

- Refactor into a loop with a list of `(question, answer)` pairs once loops are allowed
- Wrap the input parsing in `try`/`except` for invalid input
- Turn the quiz logic into a function so it can be reused or tested
- Add more questions or randomize which ones are asked