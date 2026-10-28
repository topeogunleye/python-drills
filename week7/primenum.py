n = int(input("Enter an integer N: "))

def is_prime(num):
    if num < 2:
        return False

    

if is_prime(n):
    print(f"{n} is prime.")
else:
    print(f"{n} is not prime.")

primes = []
prime_sum = 0
candidate = 2
while candidate <= n:
    if is_prime(candidate):
        primes.append(candidate)
        prime_sum += candidate
    candidate += 1

print(f"Primes up to {n}: {primes}")
print(f"Sum of primes: {prime_sum}")