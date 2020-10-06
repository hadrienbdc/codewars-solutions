def generate_primes(n):
    # Sieve of Eratosthenes algorithm
    is_prime = [False, False] + [True for x in range(2, n + 1)] 
    i = 2
    while i * i <= n:

        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
        i += 1

    primes = [x for x in range(n+1) if is_prime[x]]

    return primes


class Primes:
    n = 16000000
    all_primes = generate_primes(n)

    @staticmethod
    def stream():
        yield from Primes.all_primes
