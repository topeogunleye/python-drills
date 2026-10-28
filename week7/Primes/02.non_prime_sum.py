def is_prime(n: int) -> bool:

    if n == 2:
        return True

    
    if n < 2 or n % 2 == 0:
        return False

    i = 3

    while i < n:
        if n % i == 0:
            return False

        i += 2
        
    return True

def non_prime_sum(n):
    sum = 0
    not_prime_list = []

    for i in range(4, n + 1):
        if not is_prime(i):
            sum += i
            not_prime_list.append(i)

    print(f"{n} is prime" if is_prime(n) else f"{n} is not prime")
    print(f"Non prime numbers up to {n}: {not_prime_list}")
    print(f"Sum of primes: {sum}")

non_prime_sum(10)