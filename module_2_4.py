numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True
not_primes = []
primes = []
for i in range(len(numbers)):
    i += 1
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                not_primes.append(i)
                is_prime = False
                break
            else:
                is_prime = True
                continue
    else:
        continue
    if is_prime == True:
        primes.append(i)
print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")