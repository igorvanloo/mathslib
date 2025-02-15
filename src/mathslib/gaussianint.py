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
Implementation of Gaussian Integers

NOTE: THIS IS A WORK IN PROGRESS, NOT RECOMMENDED FOR USE YET

I provide some useful posts that I used in the creation of the code I have so far

`General method of prime factorizing a Gaussian Integer <https://stackoverflow.com/questions/2269810/whats-a-nice-method-to-factor-gaussian-integers?noredirect=1&lq=1>`_

`How to pick the correct remainder when doing division <https://math.stackexchange.com/questions/2584150/finding-values-of-quotient-and-remainders-for-gaussian-integers>`_

Author: Igor van Loo
'''
import math
from .primes import prime_factors

class GI:
    '''
    Implementation of a Gaussian Integer as a class

    '''
    def __init__(self, a, b):
        '''
        Standard init, keeps track of real and imaginary components of the Gaussian Integer

        '''
        self.value = (a, b)
        self.real = a
        self.im = b
    
    def __str__(self):
        '''
        returns string version of Gaussian integer

        '''
        a, b = self.value
        if b < 0:
            return f"{a} - {b}i"
        return f"{a} + {b}i"
    
    def __mul__(self, other):
        '''
        Defining multiplication of 2 Gaussian Integers

        '''
        a1, b1 = self.value
        if type(other) == int or type(other) == float:
            return other * GI(a1, b1)
        a2, b2 = other.value
        return GI(a1*a2 - b1*b2, a1*b2 + b1*a2)
    
    def __truediv__(self, other):
        '''
        Defining division of 2 Gaussian integers

        '''
        return (1/other.norm_sq()) * GI(self.real, self.im)*other.conj() 
    
    def __rmul__(self, scalar):
        '''
        Defining multiplication of Gaussian Integers by scalars

        '''
        a, b = self.value
        return GI(scalar*a, scalar*b)
    
    def __add__(self, other):
        '''
        Defining addition of Gaussian Integers

        '''
        a1, b1 = self.value
        a2, b2 = other.value
        return GI(a1 + a2, b1 + b2)
    
    def __sub__(self, other):
        '''
        Defining subtraction of Gaussian Integers

        '''
        a1, b1 = self.value
        a2, b2 = other.value
        return GI(a1 - a2, b1 - b2)
    
    def __eq__(self, other):
        '''
        Defining equality of Gaussian Integers

        '''
        a1, b1 = self.value
        a2, b2 = other.value
        if a1 == a2 and b1 == b2:
            return True
        return False
        
    def conj(self):
        '''
        Defining the conjugate of a Gaussian Integer

        '''
        a, b = self.value
        return GI(a, -b)
    
    def norm_sq(self):
        '''
        Defining the nrom squared of a Gaussian Integer

        '''
        a, b = self.value
        return a*a + b*b
        
    def prime_fac(self):
        '''
        Prime Factorization of a Gaussian Integer

        '''
        int_fac = prime_factors(self.norm_sq())
        gauss_fac = {}
        G = GI(self.real, self.im)
        for p in int_fac:
            e = int_fac[p]
            if p == 2:
                u = GI(1, 1)
                G /= u
                gauss_fac[str(u)] = e
            elif p % 4 == 3:
                q = GI(p, 0)
                gauss_fac[str(q)] = e//2
                G /= q
            elif p % 4 == 1:
                v = 2
                while True:
                    if pow(v, (p - 1)//2, p) == -1 % p:
                        k = pow(v, (p - 1)//4, p)
                        break
                    v += 1
                u = gcd(GI(p, 0), GI(k, 1))
                if rem(G, u).value == (0, 0):
                    q = u
                else:
                    q = u.conj()
                gauss_fac[str(q)] = e
                G /= q
        if G.value != (1, 0):
            gauss_fac[str(G)] = 1
        return gauss_fac

def rem(x, y):
    '''
    Computes the remainder when Gaussian Integer x is divided by Gaussian integer y

    '''
    a1, b1 = x.value
    a2, b2 = y.value
    n = y.norm_sq()
    
    #(a1 + ib1)/(a2 + ib2) = (a1 + ib1)(a2 - ib2)/(a2*a2 + b2*b2) = (a1*a2 + b1*b2) + i(a2*b1 - a1*b2))/n
    v0 = (a1*a2 + b1*b2)
    v1 = (a2*b1 - a1*b2)
    
    u0 = v0 // n
    u1 = v1 // n
    if u0 == 0:
        r0 = [u0]
    else:
        r0 = [u0, u0 + 1]
    
    if u1 == 0:
        r1 = [u1]
    else:
        r1 = [u1, u1 + 1]
    for i in r0:
        for j in r1:
            if abs((v0/n - i)**2 + (v1/n - j)**2) < 1:
                return x - y*GI(i, j)

def gcd(x, y):
    '''
    Computes the gcd of 2 Gaussian Integers

    '''
    a1, b1 = x.value
    a2, b2 = y.value
    while (a2, b2) != (0, 0):
        v = rem(GI(a1, b1), GI(a2, b2)).value
        (a1, b1), (a2, b2) = (a2, b2), v
    return GI(a1, b1)