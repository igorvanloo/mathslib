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
Various simple functions

Author: Igor van Loo
'''
import math

def bin_exp(a, b, c, n, m = None):
    '''
    If (a + b√(c))^n (mod m) = x + y√(c), then this function finds x, y by using binary exponentiation.

    :param a: An integer, coefficient of nonsqrt term
    :param b: An integer, coefficient of sqrt
    :param c: An integer, inside the sqrt
    :param n: An integer, exponent
    :param m: An integer, the modulus

    :returns: x, y such that (a + b√(c))^n (mod m) = x + y√(c)
        
    .. code-block:: python
        #Using fibonacci relation to golden ratio we know
        #(((1 + sqrt(5))/2)^n - ((1 + sqrt(5))/2)^n)/sqrt(5) = F(n)
        
        x = bin_exp(1/2, 1/2, 5, 10)  #x = (61.5, 27.5) represents 61.5 + 27.5*sqrt(5)
        y = bin_exp(1/2, -1/2, 5, 10) #y = (61.5, -27.5) represents 61.5 - 27.5*sqrt(5)
        
        #Therefore, F(10) = (61.5 + 27.5*sqrt(5) - (61.5 - 27.5*sqrt(5)))/sqrt(5)) = 55
        
        print(x[1] - y[1]) #55.0
        
    '''
    if m == None:
        a_res, b_res = a, b
        for bit in bin(n)[3:]:
            a_res, b_res = (a_res*a_res + c*b_res*b_res), 2*a_res*b_res
            if bit == "1":
                a_res, b_res = (a*a_res + b*c*b_res), (b*a_res + a*b_res)
    else:
        a_res, b_res = a, b
        for bit in bin(n)[3:]:
            a_res, b_res = (a_res*a_res + c*b_res*b_res) % m, 2*a_res*b_res % m
            if bit == "1":
                a_res, b_res = (a*a_res + b*c*b_res) % m, (b*a_res + a*b_res) % m
    return a_res, b_res
    
def number_to_base(n, b):
    '''
    Changes n from base 10 to base b

    :param n: An integer, number to be changed
    :param b: An integer, base in question

    :returns: n in base b
        
    .. code-block:: python
    
        print(number_to_base(10, 2)) #[1, 0, 1, 0]
        print(number_to_base(10, 3)) #[1, 0, 1]
        
    '''
    if (type(n) != int) or (type(b) != int):
        return "n and b must be an integer"
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def extended_euclidean_algorithm(a, b):
    '''
    Standard `Extended Euclidean Algorithm
    <https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode>`_

    :param a: An integer
    :param b: An integer

    :returns: A tuple (g, s, t) where gcd(a, b) = g = as + bt
    
    .. code-block:: python
    
        print(extended_euclidean_algorithm(240, 46)) #(2, -9, 47)

    '''
    if (type(a) != int) or (type(b) != int):
        return "a and b must be integers"
    old_r, r = a, b
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q*r
        old_s, s = s, old_s - q*s 
    if b != 0:
        bezout_t = (old_r - old_s*a) // b
    else:
        bezout_t = 0
    return old_r, old_s, bezout_t

def lcm(a_list):
    '''
    Finds the lcm of a list of numbers

    :param alist: A list containing integers

    :returns: The lcm of all numbers in the list
    
    .. code-block:: python
    
        print(lcm([2, 3])) #6
        print(lcm([2, 4, 5, 7])) #140
        print(lcm([8345, 23579, 174])) #34237415370
        
    '''
    n = sorted(a_list)
    curr = n.pop(-1)
    while len(n) != 0:
        temp = n.pop(-1)
        curr = int(abs(curr*temp)/math.gcd(curr, temp))
    return curr

def mod_division(a, b, m):
    '''
    Finds a/b mod m

    :param a: An integer, the numerator
    :param b: An integer, the denominator
    :param m: An integer, the modulus

    :returns: a/b mod m
    
    .. code-block:: python
    
        print(mod_division(8, 4, 5)) #2
        
    '''
    if (type(a) != int) or (type(b) != int) or (type(m) != int):
        return "n and b must be an integer"
    try:
        inv = pow(b, -1, m)
    except ValueError:
        if a % b == 0:
            answer = (a % m * b) // b
    else:
        a = a % m
        answer = (inv * a) % m
    return answer

def bisect(alist, goal):
    '''
    This function is equivalent to bisect_right from the bisect module

    :param alist: A list
    :param goal: A number

    :returns: index i of A such that A[i - 1] < g <= A[i]
    
    .. code-block:: python
    
        print(bisect([2, 3, 5, 7], 6)) #3 since A[2] = 5 < 6 <= A[3] = 7
        
    '''
    lo = 0
    hi = len(alist)
    while lo < hi:
        mid = (lo + hi)//2
        if goal < alist[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def is_clockwise(a,b,c):
    '''
    Finds if 3 points a going to b going to c are in clockwise order. It is used in convex
    hull algorithm

    :param a: A tuple, representing a point in 2D
    :param b: A tuple, representing a point in 2D
    :param c: A tuple, representing a point in 2D

    :returns: True if point are in clockwise direction, otherwise False
        
    '''
    ax, ay = a
    bx, by = b
    cx, cy = c
    if (cy - ay)*(bx - ax) < (by - ay)*(cx - ax):
        return True
    return False