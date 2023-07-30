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
Divisor related functions

Author: Igor van Loo
'''
import math
from .primes import prime_factors, spf_sieve

def divisors(n, proper = False):
    '''
    Finds all the divisors of n using the prime factorisation of n and recursion to find all divisors. 
    `Blog by numericalrecipes <https://numericalrecipes.wordpress.com/tag/divisors/>`_ is an excellent article explaining the algorithm and even faster versions.

    :param x: Integer
    :param proper: Optional boolean value, If true it will output all proper divisors of n

    :returns: A list which contains all divisors of n
    
    .. code-block:: python
    
        print(divisors(15)) #[1, 3, 5, 15]
        print(divisors(15, proper = True)) #[1, 3, 5]

    '''
    if (type(n) != int):
        return "All values must be integers"
    
    pf = prime_factors(n)
    primes = [x for x in pf]
    l = len(primes)

    def gen(n = 0):
        if n == l:
            return [1]
        else:
            pows = [1]
            p = primes[n]
            for _ in range(pf[p]):
                pows.append(pows[-1] * p)
            
            div = []
            for q in gen(n + 1):
                for p in pows:
                    div.append(q * p)
            return div
                    
    div = gen()
    if proper:
        div.pop(-1)
        return div
    return div
    
def divisor(x, n):
    '''
    Implementation of `Divisor function 
    <https://en.wikipedia.org/wiki/Divisor_function#Definition>`_ sigma(x, n) 
    
    :param x: An integer, denotes the power till which the divisors will be summed
    :param n: An integer, denotes the number to find the divisors of
    
    :returns: An integer
    
    .. code-block:: python
    
        print(divisor(0, 9)) #3, 9 has 3 divisors [1, 3, 9]
        print(divisor(1, 9)) #13 = 1 + 3 + 9
        print(divisor(2, 9)) #91 = 1*1 + 3*3 + 9*9
        
    '''
    if (type(n) != int) or (type(x) != int):
        return "All values must be integers"
    
    pf = prime_factors(n)
    total = 1
    if x == 0:
        for p in pf:
            e = pf[p]
            total *= (e + 1)
    else:
        for p in pf:
            e = pf[p]
            total *= ((pow(p, x*(e + 1)) - 1)//(pow(p, x) - 1))
    return total

def divisor_sieve(x, N):
    '''
    Implementation of `Divisor function 
    <https://en.wikipedia.org/wiki/Divisor_function#Definition>`_ sigma(x, n) sieve. 
    It returns an array such that array[x] = sigma(x, n)
    
    :param x: An integer
    :param n: An integer, denotes the length of the array
    
    :returns: An array such that array[x] = sigma(x, n)
    
    .. code-block:: python
    
        print(divisors_sieve(0, 10)) #[0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4]
        print(divisors_sieve(1, 10)) #[0, 1, 3, 4, 7, 6, 12, 8, 15, 13, 18]
        print(divisors_sieve(2, 10)) #[0, 1, 5, 10, 21, 26, 50, 50, 85, 91, 130]
    
    .. note::
        The case x = 0 is especially useful as it gives an array such that array[x] = number of divisors of x
        
    '''
    spf = spf_sieve(N)
    d = spf
    for i in range(2, N + 1):
        if spf[i] == i:
            if x == 0:
                d[i] = 2
            else:
                d[i] = 1 + pow(i, x)
        else:
            
            p = spf[i]
            t = i // p
            e = 1
            while t % p == 0:
                e += 1
                t //= p
            
            if x == 0:
                #We use the fact that d[n] = (e + 1) * d[n/p^e]
                d[i] = d[t]*(e + 1)
            else:
                #We use the fact that d[n] = (p^(x*(e + 1)) - 1)/(p^x - 1) * d[n/p^e]
                d[i] = d[t]*((pow(p, x*(e + 1)) - 1)//(pow(p, x) - 1))
    return d