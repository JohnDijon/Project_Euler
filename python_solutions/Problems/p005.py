def gcd(a, b):
    '''Euclidean algorithm, recursion'''
    if a < b:
        a, b = b, a
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)


def lowest_common_divider(div_low, div_high):
    ''' div_low: lowest num, div_high highest num to look at
        Lowest common multiple(LCM)
        Greatest common divider (GCD)
        LCD(x, y) = x * y / GCD(x, y)
        Since LCD is associative and commutative operation:
        LCD(x1, x2, x3, ...,xn) = LCD(xn, LCD(x(n-1), (LCD(..., LCD(x1,x2))...)))
        GCD can be realized by recursion (Euclidean algorithm), loop or gcd.math() method
     '''
    y = div_low
    for i in range((div_low + 1), (div_high + 1)):
        y *= i / gcd(y, i)
    return y

if __name__ == '__main__':
    print(lowest_common_divider(1, 20))
