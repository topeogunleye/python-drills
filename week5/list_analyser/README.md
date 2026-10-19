1. List Analyser — Extended
Suggested time: 12–15 minutes
Problem
Given a list of numbers, find the smallest, largest, total, and average — and also report the index of the smallest and largest values, and how many numbers are above the average.
Examples
Starting list: numbers = [12, 5, 27, 8, 14, 27, 3]
Input list: [12, 5, 27, 8, 14, 27, 3]
Smallest: 3 (at index 6)
Largest: 27 (at index 2)
Total: 96
Average: 13.71
Numbers above average: 3
Constraints
Use loops and variables to calculate all results.
Do not use min(), max(), sum(), .index(), or .count().
You may use len() for the average.
If the smallest or largest value appears more than once, report the first index where it appears.
The “numbers above average” count must be calculated in a second pass through the list (after the average is known).
Assume the list contains at least one number.
Do not hardcode the answer.
What This Tests: Lists, iteration, accumulators, comparisons, tracking indices alongside values, and two-pass algorithms.
