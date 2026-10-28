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

def prime_counter(n):
    count = 0
    prime_list = []

    i = 2

    while i < n:
        if is_prime(i):
            count += 1
            prime_list.append(i)
        i += 1

    print(f"{n} is a prime number" if is_prime(n) else f"{n} is not a prime number")
    print(f"Primes up to {n}: {prime_list}")
    print(f"Number of primes: {count}")

prime_counter(1)