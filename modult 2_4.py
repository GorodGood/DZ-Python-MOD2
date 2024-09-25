numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
sum_ = 0
for i in range(2, len(numbers) + 1):
    for j in range(2, i):
        if i % j == 0:
            sum_ = sum_ + 1
    if sum_ == 0:
        primes.append(i)
    else:
        sum_ = 0
        not_primes.append(i)
print(primes)
print(not_primes)
