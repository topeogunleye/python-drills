def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

def largest_prime_number(n: int):
    if n < 2:
        print(f"There are no prime numbers up to {n}.")
        return

    i = n

    # while i > 1:
    #     if is_prime(i):
    #         print(f"Largest prime up to {n}: {i}")
    #         return
    #     i += 1
    
    for i in range(n, 1, -1):
        if is_prime(i):
            print(f"Largest prime up to {n}: {i}")
            return

    print(f"No prime number found up to {n}.")

largest_prime_number(10)
