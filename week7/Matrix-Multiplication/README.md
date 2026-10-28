# Q23 — Matrix Multiplication

**CodeQuest · Python Foundation Challenge Set 4**  
**Part A — Revision (Harder Variant)**  
**Suggested learner solving time:** 20–25 minutes  
**Suggested recording length:** 5–7 minutes

## Challenge prompt

### Problem

Given two matrices, A and B, calculate their product matrix. Matrix multiplication is possible only if the number of columns in A equals the number of rows in B.

### Examples

```text
Matrix A: [[1, 2], [3, 4]]
Matrix B: [[5, 6], [7, 8]]
Product Matrix:
[19, 22]
[43, 50]
(Explanation: 1×5 + 2×7 = 19; 1×6 + 2×8 = 22, etc.)
```

### Constraints

- Use nested loops (three levels of loops are needed).
- Do not import libraries such as numpy.
- Do not use list comprehensions.
- Dynamically build the result matrix based on the dimensions of A and B.
- Do not hardcode the answer.

### What this tests

Advanced nested loops, matrix dimensions, indexing, and accumulators.

## Reference solution

```py
def multiply_matrices(A, B):
    if len(A) == 0 or len(B) == 0:
        return None

    rows_a = len(A)
    columns_a = len(A[0])
    rows_b = len(B)
    columns_b = len(B[0])

    if columns_a != rows_b:
        return None

    result = []
    for i in range(rows_a):
        result_row = []
        for j in range(columns_b):
            total = 0
            for k in range(columns_a):
                total += A[i][k] * B[k][j]
            result_row.append(total)
        result.append(result_row)

    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
product = multiply_matrices(A, B)

if product is None:
    print("Matrix multiplication is not possible.")
else:
    print("Product Matrix:")
    for row in product:
        print(row)
```

### Line-by-Line Explanation
- `multiply_matrices(A, B)` accepts the two matrices as data; it does not hardcode their product.
- The first `if` handles empty inputs. The next four assignments calculate the row and column counts used to size the result.
- `if columns_a != rows_b` applies the multiplication compatibility rule; `None` signals that no product can be formed.
- `result = []` starts the dynamically built output.
- The outer loop selects a row of A; `result_row = []` starts the corresponding output row.
- The middle loop selects a column of B and initializes `total` for that cell.
- The inner loop walks across the selected A row and down the selected B column. `total += A[i][k] * B[k][j]` accumulates the dot product.
- `result_row.append(total)` stores the completed cell. `result.append(result_row)` stores a completed output row.
- `return result` returns the full product. The sample matrices are then passed to the function; the final conditional prints an error for incompatible dimensions or prints each result row.

### How It Works
The sample is a 2×2 matrix multiplied by a 2×2 matrix. For the first output cell, the inner loop calculates 1×5 + 2×7 = 19. For the next cell it calculates 1×6 + 2×8 = 22. Repeating the same row-column calculation for A's second row gives 43 and 50. The dynamically built result is `[[19, 22], [43, 50]]`.

**Additional checks**

- Rectangular case: `[[1, 2, 3], [4, 5, 6]]` multiplied by `[[7, 8], [9, 10], [11, 12]]` gives `[[58, 64], [139, 154]]`.
- Incompatible case: `[[1, 2], [3, 4]]` multiplied by `[[1, 2, 3]]` is not possible because A has 2 columns and B has 1 row.

**Assumption:** Inputs are non-empty rectangular matrices containing numeric values.

## Recording focus

Matrix dimensions and the three nested loops that compute each product cell.

## NotebookLM Audio Overview prompt

> Create a 5–7 minute beginner-friendly teaching audio for this Python challenge. State the goal, restate the prompt, and explain constraints before the approach. Invite learners to pause and try first. Trace one supplied example accurately, then explain the reference code line by line and summarize how it works. Respect all stated requirements: no forbidden shortcuts, extra libraries, or invented rules. End with a short recap and one check-for-understanding question; pronounce identifiers naturally. Focus: Matrix dimensions and the three nested loops that compute each product cell.