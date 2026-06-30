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


if __name__ == '__main__':
    print(show_prime([7, 8, 13, 15, 67, 101, 199, 202, 25]))