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

def between_two_limits(s,e):

    sum = 0
    prime_list = []

    start = s
    # i = s
    while s <= e:
        if is_prime(s):
             sum += s
             prime_list.append(s)
        s += 1
            
    print(f"Primes numbers between {start} and {e}: {prime_list}")
    print(f"Sum of primes: {sum}")

between_two_limits(10, 20)