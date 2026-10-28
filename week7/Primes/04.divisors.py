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

    if is_prime(n):
        print(f"{n} is prime")
        print(f"Divisors of {n}: [1, {n}]")
        print("Number of divisors: 2")
    else:
        count = 0
        divisor_list = []

        i = 2
        while i <= n:
            if n % i == 0:
                divisor_list.append(i)
                count += 1
            i += 1

        print(f"{n} is not prime")
        print(f"Divisors of {n}: {[1, *divisor_list]}")
        print(f"Number of divisors: {count}")

prime_counter(8)