def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        this_prime = True
        if result not in (-1, 0, 1):
            for i in range(2, result):
                if result % i == 0:
                    this_prime = False
                    break

        print(['Составное', 'Простое'][this_prime])

        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(2, 3, 2))
