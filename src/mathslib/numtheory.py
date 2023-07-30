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
from .primes import prime_sieve
from .simple import extended_euclidean_algorithm

def phi(n):
    '''
    Implementation of `Eulers Totient Function
    <https://en.wikipedia.org/wiki/Euler%27s_totient_function>`_ counts the positive integers up to a given integer n that are relatively prime to n

    :param n: An integer

    :returns: An integer, numbers, a, less than n, such that gcd(a, n) = 1
    
    .. code-block:: python
    
        print(phi(20)) #8
        print(phi(100)) #40
        
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
            phi *= (pow(d, count - 1)*(d-1))
        d = d + 1
        if d*d > n:
            if n > 1: 
                phi *= int(n - 1)
            break
    return phi

def phi_sieve(n):
    '''
    A sieve for `Eulers Totient Function
    <https://en.wikipedia.org/wiki/Euler%27s_totient_function>`_ which counts the positive integers up to a given integer n that are relatively prime to n

    :param n: An integer

    :returns: An array, where array[x] = phi(x)
    
    .. code-block:: python
    
        print(phi_sieve(10)) #[0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
        print(phi_sieve(20)[11:]) #[10, 4, 12, 6, 8, 8, 16, 6, 18, 8]
        
    '''
    phi = [i for i in range(n + 1)]
    for p in range(2, n + 1):
        if phi[p] == p:
            phi[p] -= 1
            for i in range(2*p, n + 1, p):
                phi[i] -= (phi[i] // p)
    return phi

def phi_sum(n):
    '''
    Computes the `Totient Summatory Function
    <https://en.wikipedia.org/wiki/Totient_summatory_function>`_
    
    The algorithm is based on `Overview of Project Euler Problem 351 <https://projecteuler.net/overview=0351>`_
    specifically, this is an implementation of Algorithm 6, which you may view after Solving Problem 351

    :param n: An integer

    :returns: sum of phi(x) where x goes from 1 to n
    
    .. code-block:: python
    
        print(phi_sum(10**4)) #30397486
        print(sum(phi(i) for i in range(1, 10**4 + 1))) #30397486
        print(sum(phi_sieve(10**4))) #30397486
        
    '''
    L = int(math.sqrt(n))
    v = [0]*(L + 1)
    bigV = [0]*(n//L + 1)
    
    for x in range(1, L + 1):
        res = (x*(x + 1))//2
        for g in range(2, int(math.sqrt(x)) + 1):
            res -= v[x//g]
        
        for z in range(1, int(math.sqrt(x)) + 1):
            if x//z != z:
                res -= (x//z - x//(z + 1))*v[z]
        
        v[x] = res
    
    for x in range(n//L, 0, -1):
        k = n//x
        res = (k*(k + 1))//2
        
        for g in range(2, int(math.sqrt(k)) + 1):
            if k//g <= L:
                res -= v[k//g]
            else:
                res -= bigV[x*g]
        
        for z in range(1, int(math.sqrt(k)) + 1):
            if z != k//z:
                res -= (k//z - k//(z + 1))*v[z]
        bigV[x] = res
        
    return bigV[1]

def mobius(n):
    '''
    Implementation of the `Mobius function
    <https://en.wikipedia.org/wiki/M%C3%B6bius_function>`_ of n

    :param n: An integer

    :returns: An integer
    
    .. code-block:: python
    
        print(Mobius(10)) #1 - 10 = 2*5, therefore μ(10) = (-1)*(-1) = 1
        print(Mobius(9)) #0 - Divisble by 3*3
        print(Mobius(7)) #-1 - 7 is prime therefore μ(7) = -1
    
    .. note::
        * returns 0 if n is divisible by p^2, where p is a prime
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
    return pow(-1, num_of_primes)

def mobius_k_sieve(limit, k = 2):
    '''
    A sieve for the Generalized `Mobius function
    <https://en.wikipedia.org/wiki/M%C3%B6bius_function>`_, the mathematics of this function can be read
    in the following `PDF <https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-32/issue-1/M%C3%B6bius-functions-of-order-k/pjm/1102977519.pdf>`_
    Note that when k = 2 we get the normal mobius function shown above.
    
    :param limit: An integer
    :param k: Optional integer, default value is 2 which gives a regular mobius sieve

    :returns: An array where array[x] = μ(k, x)
    
    .. code-block:: python
    
        print(mobius_k_sieve(10)) #[0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1]
        print(mobius_k_sieve(10, 3)) #[0, 1, -1, -1, -1, -1, 1, -1, 0, -1, 1]
    
    '''
    isprime = [1]*(limit + 1)
    isprime[0] = isprime[1] = 0
    mob = [0] + [1]*(limit)
    for p in range(2, limit + 1):
        if isprime[p]:
            mob[p] *= -1
            for i in range(2*p, limit + 1, p):
                isprime[i] = 0
                mob[i] *= -1
            sq = pow(p, k)
            if sq <= limit:
                for j in range(sq, limit + 1, sq):
                    mob[j] = 0
    return mob

def count_k_free(n, k):
    '''
    A function that counts the integers ≤ n which are k-power free.
    count_k_free(n, 2) would count the number of squarefree integers. 
    The mechanics of this function come from this `PDF <https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-32/issue-1/M%C3%B6bius-functions-of-order-k/pjm/1102977519.pdf>`_
    
    :param n: An integer
    :param k: An integer
    
    :returns: The number of integers ≤ n which are k-power free
    
    From `Project Euler Problem 193 <https://projecteuler.net/problem=193>`_
    
    .. code-block:: python
    
        print(count_k_free(2**50, 2)) #684465067343069
        
    '''
    sq = math.floor(n**(1/k))
    mobius_k = mobius_k_sieve(sq)
    return sum([mobius_k[i]*(n//pow(i, k)) for i in range(1, sq + 1)])

def pythagorean_triples(limit, non_primitive = True):
    '''
    Generates all `Pythagorean Triplets 
    <https://en.wikipedia.org/wiki/Pythagorean_triple>`_ up to the limit

    :param limit: An integer, will generate all Pythagorean Triplets such that no side is longer than the limit
    :param non_primitive: Optional boolean value, If True, returns all triplets, if False returns only primitive triplets

    :returns: A list containing all desired triplets
    
    .. code-block:: python
        
        print(pythagorean_triples(20)) #[[3, 4, 5], [6, 8, 10], [9, 12, 15], [12, 16, 20], [5, 12, 13], [15, 8, 17]]
        print(pythagorean_triples(20, False)) #[[3, 4, 5], [5, 12, 13], [15, 8, 17]]
        print(len(pythagorean_triples(100, False))) #16
    
    '''
    if (type(limit) != int):
        return "All values must be integers"
    triples = []
    for m in range(2,int(math.sqrt(limit))+1):
        for n in range(1 + m % 2, m, 2):
            if math.gcd(m,n) == 1:
                a = m**2 + n**2
                b = m**2 - n**2
                c = 2*m*n
                if a < limit:
                    if non_primitive:
                        for k in range(1,int(limit/a)+1):
                            triples.append([k*b,k*c,k*a])
                    else:
                        triples.append([b,c,a])
    return triples

def count_primitive_pythagorean_triples(n):
    '''
    Function counts the number of primitive `Pythagorean Triplets 
    <https://en.wikipedia.org/wiki/Pythagorean_triple>`_ with hypotenuse less than n.
    Algorithm is adapted from the following paper `Pythagorean triangles with legs less than n <https://www.sciencedirect.com/science/article/pii/S0377042701004964#aep-abstract-id6>`_

    :param n: An integer

    :returns: Number of primitive Pythagorean triplets with hypotenuse less than n
    
    .. code-block:: python
        
        print(count_primitive_pythagorean_triples(10**10)) #1591549475
        print(count_primitive_pythagorean_triples(10**8)) #15915493
        
    .. note::
        Due to some precision errors the answer can somtimes be a few numbers off for example the correct answer
        for n = 10^8 is actually 15915492, one less than what my function gives.
    
    '''
    if (type(n) != int):
        return "All values must be integers"
    mu = mobius_k_sieve(int(math.sqrt(n)) + 1)
    
    R_cache = {}
    def R(n):
        if n in R_cache:
            return R_cache[n]
        c = 0 
        for x in range(int(math.sqrt(n)) + 1):
            min_y, max_y = x + 1, int(math.sqrt(n - x*x))
            if max_y < min_y:
                break
            c += max_y - min_y + 1
        R_cache[n] = c
        return c
    
    def Q(n):
        total = 0
        m = math.sqrt(n)
        for d in range(1, int(m) + 1):
            total += mu[d] * R(n // (d*d))
        return total
    
    c = 0
    k = 0
    while 2**k <= n:
        x = Q(n // pow(2, k))
        c += pow(-1, k) * x
        k += 1
    return c

def legendre_factorial(x):
    '''
    Implementation of `Legendres' Formula
    <https://en.wikipedia.org/wiki/Legendre%27s_formula>`_

    :param x: An integer

    :returns: A dictionary containing the prime factorisation of x!
    
    .. code-block:: python
    
        print(legendre_factorial(6)) #{2: 4, 3: 2, 5: 1} 
        
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
    <https://en.wikipedia.org/wiki/Smooth_number>`_ up to the limit

    :param max_prime: The maximum prime allowed
    :param limit: limit up till which to find max_prime smooth numbers

    :returns: A list containing all k ≤ max_prime smooth numbers less that limit
    
    From `Project Euler Problem 204 <https://projecteuler.net/problem=204>`_
    
    .. code-block:: python
    
        print(len(k_smooth_numbers(5, 10**8))) #1105
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

def k_powerful(k, limit, count = True):
    '''
    Find all `k-powerful numbers
    <https://en.wikipedia.org/wiki/Powerful_number>`_ less than or equal to upper_bound.
    Inspired by `Rosetta <https://rosettacode.org/wiki/Powerful_numbers#Python>`_

    :param k: k, representing k-powerful
    :param limit: limit up till which to k-powerful numbers
    :param count: Optional, Boolean

    :returns: if count is True, it counts the number of k-powerful numbers, otherwise it will return them as a list
        
    .. code-block:: python
    
        print(kpowerful(2, 10^2)) #14
        print(kpowerful(2, 10^2, False)) #[1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 72, 81, 100]
    '''
    def prime_powers(k, limit):
        ub = int(math.pow(limit, 1/k) + .5)
        res = [(1,)]
        for p in prime_sieve(ub):
            a = [p**k]
            u = limit // a[-1]
            while u >= p:
                a.append(a[-1]*p)
                u //= p
            res.append(tuple(a))
        return res
    ps = prime_powers(k, limit)
    l = len(ps)
    def generate(primeIndex, ub):
        if count:
            res = 0
        else:
            res = []
        for p in ps[primeIndex]:
            u = ub//p
            if not u:
                break
            if count:
                res += 1
            else:
                res += [p]
            for j in range(primeIndex + 1, l):
                if u < ps[j][0]:
                    break
                if count:
                    res += generate(j, u)
                else:
                    res += [p*x for x in generate(j, u)]
        return res
    if count:
        return generate(0, limit)
    else:
        return sorted(generate(0, limit))
    
def legendre_symbol(a, p):
    '''
    Finds the `legendre symbol
    <https://en.wikipedia.org/wiki/Legendre_symbol>`_ of a/p
    
    :param a: An integer
    :param p: An odd prime
    
    :results: The legendre symbol of a/p
    
    .. code-block:: python
        
        print(legendre_symbol(3, 3)) #0
        print(legendre_symbol(10, 31)) #1
        print(legendre_symbol(2, 11)) #-1
    
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
    Implementation of `Tonelli Shanks algorithm
    <https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm>`_
    
    Full credit for this alogrithm goes to `Eli Bendersky 
    <https://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python/>`_

    :param a: An integer
    :param p: An integer

    :returns: solution to x^2 = a (mod p)
    
    .. code-block:: python
    
        print(tonelli_shanks(5, 41)) #28
        
    .. note::
        
        This function solves the congruence of the form x^2 = a (mod p) and returns x. 
        Note that p - x is also a root.
    
        0 is returned if no square root exists for these a and p.
         
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
        
def chinese_remainder_theorem(a1, a2, n1, n2):
    '''
    Simple `Chinese Remiander Theorem <https://en.wikipedia.org/wiki/Chinese_remainder_theorem>`__ to solve x = a1 mod n1, x = a2 mod n2

    :param a1: An integer
    :param a2: An integer
    :param n1: An integer
    :param n2: An integer

    :returns: Unique solution to x = a1 mod n1, x = a2 mod n2
    
    .. code-block:: python
        
        #We solve x = 2 mod 3 = 3 mod 5 = 2 mod 7
        #First we solve x = 2 mod = 3 mod 5
        print(chinese_remainder_theorem(2, 3, 3, 5)) #8 
        #Then we solve x = 8 mod 15 = 2 mod 7
        print(chinese_remainder_theorem(8, 2, 15, 7)) #23 
        
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

def generalised_CRT(a1, a2, n1, n2):
    '''
    A generalised `Chinese Remiander Theorem <https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Generalization_to_non-coprime_moduli>`__ which solves for non-coprime moduli

    :param a1: An integer
    :param a2: An integer
    :param n1: An integer
    :param n2: An integer

    :returns: Unique solution to x = a1 mod n1, x = a2 mod n2
    
    .. code-block:: python
        
        print(generalised_CRT(2, 3, 3, 5)) #8, note that we can use ChineseRemainderTheorem function for this case
        print(generalised_CRT(2, 4, 4, 6)) #10
        print(generalised_CRT(3, 4, 4, 6)) #'No solution'
        
    '''
    g, u, v = extended_euclidean_algorithm(n1, n2)
    if g == 1:
        return (a1*v*n2 + a2*u*n1) % (n1*n2)
    M = (n1*n2)//g
    if a1 % g != a2 % g:
        return "No solution"
    return ((a1*v*n2 + a2*u*n1)//g) % M

def frobenius_number(*integers):
    '''
    Generates the `Frobenius Number <https://en.wikipedia.org/wiki/Coin_problem>`_ for given integers.
    
    The below algorithm is based on `Faster Algorithms for Frobenius Numbers <https://www.cis.upenn.edu/~cis511/Frobenius-numbers-Nijenhuis-Wagon.pdf>`_
    specifically, this is an implementation of their Breadth-First Method which you may find on page 9

    :param: integers

    :returns: Frobenius number 
    
    .. code-block:: python3
    
        print(frobenius_number(3, 5)) #7
        print(frobenius_number(6, 9, 20)) #43
        print(frobenius_number(1000, 1476, 3764, 4864, 4871, 7773)) #47350
        
    '''
    #Set is first sorted
    A = sorted(integers) 
    #Initalize n value for future reference
    n = len(A) 
    #Initalize a1 and an for readability
    a1 = A[0]
    an = A[n - 1]
    #Step 1
    #Initalize FIFO queue
    Q = [0]
    #Initalize P
    P = [0]*a1
    P[0] = n
    #Initalize S, label vector, in which each currently known minimal path weight to a vertex is stored.
    S = [a1*an]*a1
    S[0] = 0
    #initalize Amod
    Amod = [a % a1 for a in A]
    #Step 2
    while len(Q) != 0:
        #Step 2a
        v = Q.pop(0) #Remove the head of Q and set it to the vertex v
        #Step 2b
        for j in range(2, P[v] + 1):
            #Step 2bi
            u = v + Amod[j - 1]
            if u >= a1:
                u -= a1
            #Step 2bii
            w = S[v] + A[j - 1]
            #Step 2biii
            if w < S[u]:
                S[u] = w
                P[u] = j
                if u not in Q:
                    Q.append(u)
    #Step 3
    return max(S) - a1

def continued_fraction(x):
    '''
    Finds the `continued Fraction
    <https://en.wikipedia.org/wiki/Continued_fraction>`_ of the sqrt(x)

    :param x: An integer

    :returns: A list containing the continued fraction of x
    
    .. code-block:: python
    
        print(continued_fraction(19)) #[4, 2, 1, 3, 1, 2, 8]
    
    .. note::
        
        The continued fraction may repeat forever, the code stops once it repeats, otherwise once we find the 100th number in the continued fraction
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
        if an == 2*math.floor(math.sqrt(x)):
            break
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
    
        print(overall_fraction([4, 2, 6, 7])) #(415, 93)

    '''
    cf = cf[::-1]
    denominator = 1
    numerator = cf[0]
    for x in range(1,len(cf)):
        numerator, denominator = cf[x]*numerator + denominator, numerator
    return numerator, denominator

