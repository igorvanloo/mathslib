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
from .primes import prime_factors, Prime_Sieve

def divisors_of(x, include_x = True):
    '''
    Finds all the divisors of x

    Parameters
    ----------
    x : An integer

    Returns
    -------
    divisors : a list containing all the divisors of x

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
    Implementation of Divisor function σ_x(n) (See here: https://en.wikipedia.org/wiki/Divisor_function#Definition)

    Parameters
    ----------
    x : An integer,
        x = 0 - Gives you number of divisors
        x = 1 - Gives you sum of divisors
        x = 2 - Gives you sum of divisors squared
    n : An integer, number to function σ_x of

    Returns
    -------
    total : Returns σ_x(n)

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
    Finds the continued Fraction of the sqrt(x)
    See here: https://en.wikipedia.org/wiki/Continued_fraction

    Parameters
    ----------
    x : An integer

    Returns
    -------
    temp_list : A list
                Contains the continued fraction of n
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
    Parameters
    ----------
    cf : list
        Takes a list containing the continued fraction of a number, returns the fraction

    Returns
    -------
    denominator : TYPE
        DESCRIPTION.
    numerator : TYPE
        DESCRIPTION.

    '''
    cf = cf[::-1]
    denominator = 1
    numerator = cf[0]
    for x in range(1,len(cf)):
        numerator, denominator = cf[x]*numerator + denominator, numerator
    return numerator, denominator

def phi(n):
    '''
    Eulers Totient Function counts the positive integers up to a given integer n that are relatively prime to n
    See here: https://en.wikipedia.org/wiki/Euler%27s_totient_function

    Parameters
    ----------
    n : An integer

    Returns
    -------
    The number of integers, a, less than n, such that gcd(a, n) = 1
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
    Finds the mobius function of n
    See here: https://en.wikipedia.org/wiki/M%C3%B6bius_function

    Parameters
    ----------
    n : An integer

    Returns
    -------
    returns 0 if n is divisible by p^2
    otherwise returns (-1)^k, where k is number of distinct prime factors
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
    Generates all Pythagorean Triplets up till the limit
    See here: https://en.wikipedia.org/wiki/Pythagorean_triple

    Parameters
    ----------
    limit : TYPE
        DESCRIPTION.
    non_primitive : Optional
                    If you want only primitive pythagorean Triplets set this to False

    Returns
    -------
    triples : A list containing all your desired type of triplets (Based on non_primitive)
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
    Implementation of Legendres' Formula
    See here: https://en.wikipedia.org/wiki/Legendre%27s_formula

    Parameters
    ----------
    x : An integer

    Returns
    -------
    Returns a list containing the prime factorisation of x!
    '''
    if (type(x) != int):
        return "All values must be integers"
    primes = Prime_Sieve(x)
    prime_fac = {}
    for y in primes:
        total = 0
        for i in range(1, int(math.floor(math.log(x,y))) + 1):
            total += int(math.floor(x/(y**i)))
        prime_fac[y] = total
    return prime_fac

def k_smooth_numbers(max_prime, limit):
    '''
    Find all k ≤ max_prime smooth numbers up till a limit
    See here: https://en.wikipedia.org/wiki/Smooth_number

    Parameters
    ----------
    max_prime : A prime
    limit : An integer

    Returns
    -------
    A list containing all k ≤ max_prime smooth numbers less that limit
    '''
    if (type(max_prime) != int) or (type(limit) != int):
        return "All values must be integers"
    k_s_n = [1]
    p = Prime_Sieve(max_prime)
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
    Finds the legendre symbol of a/p
    See here: https://en.wikipedia.org/wiki/Legendre_symbol

    Parameters
    ----------
    a : An integer
    p : An odd prime

    Returns
    -------
    Returns the legendre symbol of a/p: 
    1 if a is a quadratic residue modulo p and p does not divide a
    -1 if a is a non-quadratic residue modulo p
    0 if p divides a
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
    Credit to: https://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python/
    Implementation of Tonelli Shanks algorithm
    See here: https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm

    Parameters
    ----------
    a : An integer
    p : An integer

    Returns
    -------
    Solve the congruence of the form:
        x^2 = a (mod p)
    And returns x. Note that p - x is also a root.

    0 is returned is no square root exists for
    these a and p.
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
    Simple Chinese Remiander Theorem to solve x = a1 mod n1, x = a2 mod n2

    Parameters
    ----------
    a1 : An integer
    a2 : An integer
    n1 : An integer
    n2 : An integer

    Returns
    -------
    Unique solution x = a1 mod n1, x = a2 mod n2
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


