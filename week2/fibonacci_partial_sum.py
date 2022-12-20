def fibonacci_number(n):
    if n <= 1:
        return n
    cache = [0] * n
    cache[0] = 0
    cache[1] = 1

    for i in range(2,n):

        cache[i] = (cache[i-2] + cache[i-1]) % 10

    return cache[n-1] + cache[n-2] 
def slow_fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def fibonacci_partial_sum(from_, to):
    
    arr = [] 
    for i in range(from_, to):
        arr.append(fibonacci_number(i))

    result = 0 
    for a in arr:
        result += a

    return (result + fibonacci_number(to)) % 10


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(fibonacci_partial_sum(a,b))
