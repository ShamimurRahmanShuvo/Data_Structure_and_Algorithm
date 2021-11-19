# Calculate the sum of a list of numbers

def sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum(numbers[1:])

# Convert Integer to string in any base

def string_conversion(num, base):
    conv = "0123456789ABCDEF"

    if num < base:
        return conv[num]

    else:
        return string_conversion(num // base, base) + conv[num % base]

# Recursion List Sum

def recursive_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total = total + recursive_sum(element)
        else:
            total = total + element
    return total

# Factorial of non-negative integer

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * (factorial(number - 1))

# Fibonacci sequence

def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    else:
        return (fibonacci(n - 1) + (fibonacci(n - 2)))

# Sum of non-negative integers:

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

# Sum of a sequence n + (n-2) + (n-4) + ....

def sum_series(num):
    if num <= 1:
        return 0
    else:
        return num + sum_series(num - 2)

# Harmonic sum of n - 1

def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n-1))

# Geometric Sum

def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(2, n)) + geometric_sum(n - 1)

# value of a to the power b

def power(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

# GCD of two integers:

def gcd(a, b):
    low = min(a, b)
    high = max(a, b)
    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return gcd(low, high % low)

if __name__ == '__main__':
    print("Sum of the List:", sum([4,5,6]))
    print("Integer to string: ", string_conversion(3451, 16))
    print("List sum: ", recursive_sum([2, 3, [4, 5], [6, 7]]))
    print("Factorial: ", factorial(5))
    print("Fibonacci: ", fibonacci(10))
    print("Sum of digits:", sum_digits(546))
    print("sum of the series: ", sum_series(6))
    print("Harmonic sum: ", harmonic_sum(7))
    print("Geometric sum: ", geometric_sum(7))
    print("Power of a to b:", power(5,6))
    print("GCD: ", gcd(12, 20))

