def slow_lcm(a, b):
    for m in range(1, a * b + 1):
        if m % a == 0 and m % b == 0:
            return m

    assert False

def lcm(a, b):
    gcd_ = gcd(a,b)
    return (a * b)//gcd_

def gcd(a, b):
    if b == 0 :
        return a
    remainder = a % b
    return gcd(b, remainder)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
  

