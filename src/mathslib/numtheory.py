# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>

'''
Various Number Theory functions

Author: Igor van Loo
'''
import math
from .primes import prime_factors, prime_sieve

def divisors_of(x, include_x = True):
    '''
    Finds all the divisors of x

    :param x: Integer to be checked
    :param include_x: Optional boolean value, If true it will include x as a divisor of x

    :returns: list, contains all divisors of x

    '''
    if (type(x) != int):
        return "All values must be integers"
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))
    if include_x:
        return divisors
    else:
        divisors.remove(x)
        return divisors
    
def divisor(x, n):
    '''
    Implementation of `Divisor function 
    <https://en.wikipedia.org/wiki/Divisor_function#Definition>`_ sigma(x, n) 
    
    :param x: An integer, denotes the power till which the divisors will be summed
    :param n: An integer, denotes the number to find the divisors of
    
    :returns: An integer
    
    .. note::
        * divisor(0, n) = number of divisors of *n*
        * divisor(1, n) = sum of divisors of *n*
        * divisor(2, n) = sum of divisors squared of *n*
        
    '''
    if (type(n) != int) or (type(x) != int):
        return "All values must be integers"
    total = 1
    pf = prime_factors(n)
    for p in pf:
        e = pf[p]
        total *= ((pow(p, x*(e + 1)) - 1)//(pow(p, x) - 1))
    return total

def continued_fraction(x):
    '''
    Finds the `continued Fraction
    <https://en.wikipedia.org/wiki/Continued_fraction>`_ of the sqrt(x)

    :param x: An integer

    :returns: A list containing the continued fraction of n
    
    .. note::
        √19 = [4,2,1,3,1,2,8,2,1,3,1,2,8,...] as per Wikipedia
    
    '''
    if (type(x) != int):
        return "All values must be integers"
    m0 = 0
    d0 = 1
    a0 = math.floor(math.sqrt(x)) #These are the starting values
    temp_list = [a0]
    while True:
        mn = int(d0*a0 - m0) 
        dn = int((x - mn**2)/d0)
        an = int(math.floor((math.sqrt(x) + mn) / dn)) #new values
        temp_list.append(an)
        #if an == 2*math.floor(math.sqrt(x)):
            #break
        if len(temp_list) == 100:
            break
        m0 = mn
        d0 = dn
        a0 = an #Replace values
    return temp_list

def overall_fraction(cf):
    '''
    :param cf: A list, this list represents the continued fraction of a number

    :returns numerator: An integer, the numerator of the fraction
    :returns denominator: An integer, the denominator of the fraction
    
    .. code-block:: python
    
        overall_fraction([4, 2, 6, 7]) = 415, 93 

    '''
    cf = cf[::-1]
    denominator = 1
    numerator = cf[0]
    for x in range(1,len(cf)):
        numerator, denominator = cf[x]*numerator + denominator, numerator
    return numerator, denominator

def phi(n):
    '''
    Implementation of `Eulers Totient Function
    <https://en.wikipedia.org/wiki/Euler%27s_totient_function>`_ counts the positive integers up to a given integer n that are relatively prime to n

    :param n: An integer

    :returns: An integer, numbers, a, less than n, such that gcd(a, n) = 1
    '''
    if (type(n) != int):
        return "All values must be integers"
    if n == 1:
        return 1
    phi = 1
    d = 2 
    while n > 1:
        count = 0 
        while n % d == 0:
            count += 1
            n /= d
        if count > 0:
            phi *= (d**(count-1))*(d-1)
        d = d + 1
        if d*d > n:
            if n > 1: 
                phi *= int(n - 1)
            break
    return phi

def Mobius(n):
    '''
    Implementation of the `Mobius function
    <https://en.wikipedia.org/wiki/M%C3%B6bius_function>`_ of n

    :param n: An integer

    :returns: An integer
    
    .. note::
        * returns 0 if n is divisible by p^2
        * returns (-1)^k, where k is number of distinct prime factors
    '''
    if (type(n) != int):
        return "All values must be integers"
    if n == 1:
        return 1
    d = 2
    num_of_primes = 0
    while n > 1:
        while n % d == 0:
            num_of_primes += 1
            if n % (d*d) == 0:
                return 0
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                num_of_primes += 1
            break
    return (-1)**num_of_primes

def ppt(limit, non_primitive = True):
    '''
    Generates all `Pythagorean Triplets 
    <https://en.wikipedia.org/wiki/Pythagorean_triple>`_ up till the limit

    :param limit: An integer, will generate all Pythagorean Triplets such that no side is longer than the limit
    :param non_primitive: Optional boolean value, If True, returns all triplets, if False returns only primitive triplets

    :returns: A list containing all desired triplets
    
    '''
    if (type(limit) != int):
        return "All values must be integers"
    triples = []
    for m in range(2,int(math.sqrt(limit))+1):
        for n in range(1,m):
            if (m+n) % 2 == 1 and math.gcd(m,n) == 1:
                a = m**2 + n**2
                b = m**2 - n**2
                c = 2*m*n
                p = max(a,b,c)
                if non_primitive:
                    for k in range(1,int(limit/p)+1):
                        triples.append([k*b,k*c,k*a])
    return triples

def legendre_factorial(x):
    '''
    Implementation of `Legendres' Formula
    <https://en.wikipedia.org/wiki/Legendre%27s_formula>`_

    :param x: An integer

    :returns: A dictionary containing the prime factorisation of x!
    
    .. code-block:: python
    
        legendre_factorial(6) = {2: 4, 3: 2, 5: 1} 
        
    '''
    if (type(x) != int):
        return "All values must be integers"
    primes = prime_sieve(x)
    prime_fac = {}
    for y in primes:
        total = 0
        for i in range(1, int(math.floor(math.log(x,y))) + 1):
            total += int(math.floor(x/(y**i)))
        prime_fac[y] = total
    return prime_fac

def k_smooth_numbers(max_prime, limit):
    '''
    Find all k ≤ max_prime `smooth numbers
    <https://en.wikipedia.org/wiki/Smooth_number>`_ up till a limit

    :param max_prime: The maximum prime allowed
    :param limit: limit up till which to find max_prime smooth numbers

    :returns: A list containing all k ≤ max_prime smooth numbers less that limit
    '''
    if (type(max_prime) != int) or (type(limit) != int):
        return "All values must be integers"
    k_s_n = [1]
    p = prime_sieve(max_prime)
    while len(p) != 0:
        temp_k_s_n = []
        curr_p = p.pop(0)
        power_limit = int(math.log(limit, curr_p)) + 1
        curr_multiples = [curr_p**x for x in range(1, power_limit + 1)]
        for x in curr_multiples:
            for y in k_s_n:
                temp = x*y
                if temp <= limit:
                    temp_k_s_n.append(temp)
        k_s_n += temp_k_s_n
    return k_s_n

def legendre_symbol(a, p):
    '''
    Finds the `legendre symbol
    <https://en.wikipedia.org/wiki/Legendre_symbol>`_ of a/p
    
    :param a: An integer
    :param p: An odd prime
    
    :results: The legendre symbol of a/p
    
    .. note::
        * returns 1 if a is a quadratic residue modulo p and p does not divide a
        * returns -1 if a is a non-quadratic residue modulo p
        * returns 0 if p divides a
    
    '''
    if (type(a) != int) or (type(p) != int):
        return "All values must be integers"
    if p == 2:
        return "p must be an odd prime"
    t = pow(a, (p-1)//2, p)
    if t == p - 1:
        return -1
    return t

def tonelli_shanks(a, p):
    '''
    Credit to: 
    Implementation of `Tonelli Shanks algorithm
    <https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm>`_
    
    Full credit for this alogrithm goes to `Eli Bendersky 
    <https://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python/>`_

    :param a: An integer
    :param p: An integer

    :returns: solution to x^2 = a (mod p)
    
    .. note::
        
        This function solves the congruence of the form x^2 = a (mod p) and returns x. 
        Note that p - x is also a root.
    
        0 is returned if no square root exists for these a and p.
        
    .. code-block:: python
    
        tonelli_shanks(5, 41) = 28 
    '''
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1)//4, p)
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1
    s = int(s)
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    x = pow(a, (s + 1)//2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e
    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)
        if m == 0:
            return x
        gs = pow(g, 2**(r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m
        
def ChineseRemainderTheorem(a1, a2, n1, n2):
    '''
    Simple `Chinese Remiander Theorem
    <https://en.wikipedia.org/wiki/Chinese_remainder_theorem>`_ to solve x = a1 mod n1, x = a2 mod n2

    Parameters
    ----------
    :param a1: An integer
    :param a2: An integer
    :param n1: An integer
    :param n2: An integer

    :returns: Unique solution to x = a1 mod n1, x = a2 mod n2
    '''
    if (type(a1) != int) or (type(a2) != int) or (type(n1) != int) or (type(n2) != int):
        return "All values must be integers"
    if a1 > n1 or a2 > n2:
        return "Wrong values were input"
    #x = a1 (mod n1)
    #x = a2 (mod n2)
    #We find p = n1^-1 (mod n2), q = n2^-1 (mod n1)
    p, q = pow(n1, -1, n2), pow(n2, -1, n1)
    #The unique solution to this system is a1*q*n2 + a2*p*n1 % n1*n2
    return (a1*q*n2+ a2*p*n1) % (n1*n2)


