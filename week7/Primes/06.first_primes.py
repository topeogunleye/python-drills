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

def first_n_primes(n):

    sum = 0
    prime_list = []
    count = 0

    i = 2

    while count < n:
        if is_prime(i):
            prime_list.append(i)
            count += 1
            sum += i
        i += 1
       
    if n == 1:
        print(f"First {n} prime number: {prime_list}")
    else:
        print(f"First {n} prime numbers: {prime_list}")
    print(f"Sum of primes: {sum}")

first_n_primes(5)