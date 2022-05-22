'''
Prime Related functions
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

