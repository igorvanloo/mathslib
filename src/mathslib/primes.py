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
Prime related functions

Author: Igor van Loo
'''
import math

def prime_sieve(limit, segment = False, values = True):
    '''
    A prime sieve I made with a few different options
    

    :param limit: The limit up till which the function will generate primes
    :param segment: Optional boolean value, if segment == True, it will perform a segmented sieve 
    :param values: Optional boolean value, if values == False, it will return an array such that array[x] = True if x is prime

    :returns: All primes < limit
    
    .. code-block:: python
    
        prime_sieve(50) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        prime_sieve(10, values = False) = [False, False, True, True, False, True, False, True, False, False, False]
        
        [i for (i, isprime) in enumerate(prime_sieve(10, values = False)) if isprime] = [2, 3, 5, 7]
        
    '''
    if (type(limit) != int) or (type(segment) != bool) or (type(values) != bool):
        return "n must be an integer"
    
    if segment:
        primes = []
        sqrtN = int(math.sqrt(limit))
        result = [True]*(sqrtN + 2)
        result[0] = result[1] = False
        for i in range(2, sqrtN + 1):
            if result[i]:
                primes.append(i)
                for j in range(2*i, sqrtN + 1, i):
                    result[j] = False
        all_primes = []
        marker = [0]*len(primes)
        block_size = sqrtN
        for k in range(1, limit//block_size):
            block_start = k*block_size + 1
            block_end = (k + 1)*block_size
            curr_result = [True]*block_size
            if k == 1:
                for p_index, p in enumerate(primes):
                    count = 0
                    while (block_start + count) % p != 0:
                        count += 1
                    for j in range(block_start + count, block_end + 1, p):
                        curr_result[j - block_start] = False
                        marker[p_index] = j
            else:
                for p_index, p in enumerate(primes):
                    for j in range(marker[p_index] + p, block_end + 1, p):
                        curr_result[j - block_start] = False
                        marker[p_index] = j
            if values:
                all_primes += [block_start + i for (i, isprime) in enumerate(curr_result) if isprime]
            else:
                all_primes = all_primes[:block_start + 1] + curr_result
        if values:
            return primes + all_primes
        else:
            return result[:sqrtN + 1] + all_primes
    else:
       	result = [True] * (limit + 1)
       	result[0] = result[1] = False
       	for i in range(int(math.sqrt(limit)) + 1):
       		if result[i]:
       			for j in range(2 * i, len(result), i):
       				result[j] = False
        if values:
            return [i for (i, isprime) in enumerate(result) if isprime]
        else:
            return result

def is_prime(x):
    '''
    A simple is prime function, checks if a number is prime

    :param x: An integer

    :returns: True if x is prime, False otherwise
    
    .. code-block:: python
    
        is_prime(10) = False
        is_prime(160517089) = True
        
    '''
    if type(x) != int:
        return "x must be an integer"
    
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True

def prime_factors(n):
    '''
    Finds all the prime factors of n

    :param n: An integer

    :returns: A dictionary containing the prime divisors as keys and value as the corresponding exponent of the prime
    
    .. code-block:: python
        
        prime_factors(123123) = {3: 1, 7: 1, 11: 1, 13: 1, 41: 1}
        prime_factors(1123619623) = {7: 1, 160517089: 1}
        
    '''
    if type(n) != int:
        return "n must be an integer"
    
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                if d in factors:
                    factors[n] += 1
                else:
                    factors[n] = 1
            break
    return factors

def primepi(limit):
    '''
    Primepi function is commonly known as `Prime Counting Function <https://en.wikipedia.org/wiki/Prime-counting_function>`_
    
    This function generates an array such that array[x] = primepi(x)

    :param limit: An integer, 

    :returns: An array length limit such that array[x] = primepi(x)
    
    .. code-block:: python
    
        primepi(10) = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4]
        
    '''
    if type(limit) != int:
        return "limit must be an integer"
    
    prime_gen = prime_sieve(limit + 50, values = False)
    primes = [x for x in range(len(prime_gen)) if prime_gen[x]]
    array = [0]*(limit+1)
    p_index = 0
    for x in range(1, limit + 1):
        while True:
            if primes[p_index] > x:
                array[x] = p_index
                break
            p_index += 1
    return array

def sum_of_primes(n):
    '''
    Ultra fast sum of Primes made by Lucy The HedgeHog on Project Euler
    
    You may view it `here <https://projecteuler.net/thread=10;page=5#111677>`_ once you've completed problem 10

    :param n: An integer

    :returns: The sum of all primes up till n
    
    .. code-block:: python
        
        sum_of_primes(2*10**6) = 142913828922
        sum_of_primes(10**10) = 2220822432581729238
    '''
    if type(n) != int:
        return "n must be an integer"
    
    r = int(n ** 0.5)
    assert r * r <= n and (r + 1) ** 2 > n
    V = [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    S = {i: i * (i + 1) // 2 - 1 for i in V}
    for p in range(2, r + 1):
        if S[p] > S[p - 1]:  # p is prime
            sp = S[p - 1]  # sum of primes smaller than p
            p2 = p * p
            for v in V:
                if v < p2: break
                S[v] -= p * (S[v // p] - sp)
    return S[n]

def fermat_primality_test(n):
    '''
    A `Fermat Primality Test <https://en.wikipedia.org/wiki/Fermat_primality_test>`_

    :param n: An integer to be tested

    :returns: True if n is probably prime
    
    .. code-block:: python
    
        fermat_primality_test(17969800575241) = True #Actually True
        fermat_primality_test(101101) = True #Wrong 101101 is not prime
        
    .. note::
        This function will always guess a prime correctly due to Fermats Theorem, but may guess a composite to be a prime.
        Therefore, it is very useful when we test large numbers, otherwise it is dangerous to use. 
        
        You can test more terms to make it more and more accurate

    '''
    if type(n) != int:
        return "n must be an integer"
    
    if n < 10**5:
        print("switching to is_prime function for safety")
        return is_prime(n)
    
    else: 
        if pow(4, n - 1, n) == 1 and pow(6, n - 1, n) == 1:
            return True
        return False
