"""
This little module contains some functions that will be useful for solving
the Euler problems.
"""

def gcd(a: int, b: int) -> int:
    """ Recursive algorithm of Euklid """
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if a < b:
        tmp = a
        a = b
        b = tmp
        
    if a % b == 0:
        return(b)
    return(gcd(b, a % b))

def getFibonacciList(n: int):
    """ create a list of n consecutive Fibonacci-Numbers """
    F = [1,2]
    if n < 3:
        return(F)
    for i in range(3, n + 1):
        F.append(sum(F[-2:]))
    return(F)
    
def getFibonacci(n: int):
    """ create a list of Fibonacci-Numbers up to a certain number """
    F = [1,2]
    if n < 3:
        return(F)
    while sum(F[-2:]) < n:
        F.append(sum(F[-2:]))
    return(F)


if __name__ == '__main__':
    print('main')
    print(gcd(12, -144))
    print(getFibonacciList(10))
    print(getFibonacci(4000000))
    
    
    
    
    
    