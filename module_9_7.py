def is_prime(func):
    def wrapper(a, b, c):
        n = func(a, b, c)
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        if count == 2:
            print('Простое')
        else:
            print('Составное')
        return n
    return wrapper

@is_prime
def sum_three(a, b, c):
    n = a + b + c
    return n
result = sum_three(1, 10, 100)
print(result)