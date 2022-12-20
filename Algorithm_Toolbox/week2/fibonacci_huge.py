def slow_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci_huge_naive(n, m):
    current = fibonacci_number(n)
    return current % m

def fibonacci_number(n):
    cache = [None] * n
    cache[0] = 0
    cache[1] = 1

    for i in range(2,n):

        cache[i] = cache[i-2] + cache[i-1]
    
    return cache[n-1] + cache[n-2]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))

