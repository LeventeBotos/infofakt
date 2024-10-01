def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

primes_up_to_1000 = list_primes(1000)
f = open("output.txt", "w")
for prime in primes_up_to_1000:
    f.write(str(prime) + "\n")
f.close()
print(primes_up_to_1000)
