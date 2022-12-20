def slow_fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number(n):
    if n <= 1:
        return n
    cache = [None] * n
    cache[0] = 0
    cache[1] = 1

    for i in range(2,n):

        cache[i] = cache[i-2] + cache[i-1]

    return cache[n-1] + cache[n-2]



if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
