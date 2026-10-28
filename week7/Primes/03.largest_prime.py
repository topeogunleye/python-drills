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

def largest_prime_number(n):

    if n == 1:
        print(f"1 is not a prime number")

    if is_prime(n):
        print(f"{n} is a prime number")
        print(f"Largest prime up to {n}: {n}")
        return
    else:
        i = n - 1
        while i >= 1:
            if is_prime(i):
                print(f"{i} is a prime number")
                print(f"Largest prime up to {n}: {i}")
                break
            else:
                print(f"{i} is not a prime number")
            i -= 1
            
            print("No prime number found")

largest_prime_number(1)