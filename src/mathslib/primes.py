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

def Prime_Sieve(limit, block_size = 0, segment = False, values = True):
    '''
    A prime sieve I made with a few different options
    
    Parameters
    ----------
    limit : The limit up till which the function will generate primes
    block_size : Decide which length of blocks you would like to cut the sieve into, automatically it is set to sqrt(limit)
    segment : Decide whether you would like to use a segmented sieve or a regular sieve, it is normally set it False
    values : If segment == False, if you would like an actual list of prime then values is true, if you would
            like an array such that array[x] = True if x is prime, then set values = False

    Returns
    -------
    Based on above, all primes less than limit or an array such that array[x] = True if x is prime
    '''
    if segment:
        primes = []
        sqrtN = int(math.sqrt(limit))
        result = [True]*(sqrtN + 2)
        for i in range(2, sqrtN + 1):
            if result[i]:
                primes.append(i)
                for j in range(2*i, sqrtN + 1, i):
                    result[j] = False
        all_primes = []
        marker = [0]*len(primes)
        if block_size == 0:
            block_size = sqrtN
        for k in range(1, limit//block_size):
            if k % 100 == 0:
                print(k, limit//block_size)
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
            all_primes += [block_start + i for (i, isprime) in enumerate(curr_result) if isprime]
        return primes + all_primes
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

    Parameters
    ----------
    x : The number to be checked

    Returns
    -------
    True if x is prime
    False if x is not prime
    '''
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(5, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True

def prime_factors(n):
    '''
    Finds all the prime factors of n

    Parameters
    ----------
    n : Finds the prime factors of n

    Returns
    -------
    A dictionary containing the prime divisors as keys and value as the corresponding exponent of the prime
    '''
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
    Primepi function is commonly known as Prime Counting Function (see here: https://en.wikipedia.org/wiki/Prime-counting_function)
    
    This function generates an array such that array[x] = primepi(x)

    Parameters
    ----------
    limit : An integer, it will generate an array of length limit

    Returns
    -------
    array : array[x] = primepi(x)
    '''
    prime_gen = Prime_Sieve(limit + 50, values = False)
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

    Parameters
    ----------
    n : An integer, will sum primes up till n

    Returns
    -------
    The sum of all primes up till n
    '''
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

