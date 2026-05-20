def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True  # moved outside the for loop


def show_prime(numbers):
    primes = []
    for number in numbers:
        if check_prime(number):
            primes.append(number)
    return primes


print(show_prime([1, 4, 7, 21, 45, 67, 90, 101]))