def fibonacci_number(n):
    if n <= 1:
        return n
    cache = [None] * n
    cache[0] = 0
    cache[1] = 1

    for i in range(2,n):

        cache[i] = (cache[i-2] + cache[i-1])%10
    
    return cache[n-1] + cache[n-2]

def fibonacci_last_digit(n):
    result = fibonacci_number(n)

    return result % 10



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
    


