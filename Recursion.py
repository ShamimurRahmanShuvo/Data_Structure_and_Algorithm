# Sum of numbers using recursion

def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(4))

    tuple = ('abcd', 786, 2.23, 'john', 70.2)
    a = [1, 2, 3, None, (), [], ]
    print (type(1J))