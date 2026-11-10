def is_prime(n):
    if n < 2:
        return False

    d = 2

    while d * d <= n:
        if n % d == 0:
            return False

        d += 1

    return True

print("Primes below 50:", end=" ")

for n in range(50):
    if is_prime(n):
        print(n, end=" ")

count = 0
for n in range(100):
    if is_prime(n):
        count += 1

print("\nNumber of primes below 100:", count)

def goldbach(n):
    for p in range(2, n // 2 + 1):
        q = n - p

        if is_prime(p) and is_prime(q):
            return p, q
        else:
            continue

for n in range(4, 31, 2):
    p, q = goldbach(n)

    print(n, "=", p, "+", q)

output = True

for n in range(4, 10001, 2):

    if goldbach(n) is None:
        output = False

        print("Counter-example:", n)
        break

print("Goldbach holds for every even number from 4 to 10000:", output)