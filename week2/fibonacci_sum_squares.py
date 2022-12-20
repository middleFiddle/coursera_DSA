def fibonacci_number(n):
    if n <= 1:
        return n
    cache = [None] * n
    cache[0] = 0
    cache[1] = 1

    for i in range(2,n):

        cache[i] = (cache[i-2] + cache[i-1]) % 10

    return cache[n-1] + cache[n-2]

def slow_fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    arr = [0] * n
    for i in range(0,n):
        arr[i] = fibonacci_number(i)

    squared = list(map(lambda x: x*x, arr))

    result = 0 
    for a in squared:
        result += a

    return (result + (fibonacci_number(n)*fibonacci_number(n))) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
