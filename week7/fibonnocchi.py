def fibonacci_iterative(n: int) -> list[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    
    # Generate the rest of the terms up to n
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    
    print(f"Sequence: {', '.join(map(str, sequence))}")


    sum = 0
    for c in sequence:
        if c % 2 == 0:
            sum += c

    print(f"Even Sum: {sum}")


    print(f"Reversed: {', '.join(map(str, reversed(sequence)))}")

fibonacci_iterative(12)

