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

def prime_checker(n: int):
    prime_numbers = []
    prime_total = 0 

    for i in range(2, n) :
        if is_prime(i):
            prime_numbers.append(i)
            prime_total += i

    return prime_total, prime_numbers


print(is_prime(13))