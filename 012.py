import math


def get_divisors(number):
    divisors = set()
    for divisor in range(1, int(math.sqrt(number)+1)):
        if number % divisor == 0:
            divisors.add(divisor)
            divisors.add(number/divisor)
    print(len(divisors))
    return divisors


if __name__ == "__main__":
    current_number = 1
    sum = 0
    number_of_divisors = 0

    while 1:
        sum += current_number
        if len(get_divisors(sum)) > 500:
            print(sum)
            break
        current_number += 1
