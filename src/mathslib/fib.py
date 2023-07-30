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
Fibonacci related functions

Author: Igor van Loo
'''

def fibonacci(n, m = None):
    '''
    Finds the n-th Fibonacci using matrix exponentiation by squaring
    Method is outlined `here <http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/fastexp.pdf>`__
    Specifically, this is an implementation of the third algorithm.
    
    Also includes an option to calculate with a given modulus

    :param n: An integer
    :param m: An integer, default is None, if specificed will find F(n) (mod m)

    :returns: The n-th Fibonacci number (modulus m if specified)
    
    .. code-block:: python
    
        print(fibonacci(100)) #354224848179261915075
        print(fibonacci(100, 10**7 + 9)) #5475613
        
    '''
    if type(n) != int:
        return "n must be an integer"
    
    if m != None:
        f2, f1, f0 = 1, 1, 0
        for bit in bin(n)[3:]:
            v = (f1*f1) % m
            f2, f1, f0 = (f2 * f2 + v) % m, ((f2 + f0) * f1) % m, (v + f0 * f0) % m
            if bit == '1':
                f2, f1, f0 = f2 + f1, f2, f1 
    else:
        f2, f1, f0 = 1, 1, 0
        for bit in bin(n)[3:]:
            v = f1*f1
            f2, f1, f0 = f2 * f2 + v, (f2 + f0) * f1, v + f0 * f0
            if bit == '1':
                f2, f1, f0 = f2 + f1, f2, f1   
    return f1

def fib_till(limit):
    '''
    Finds all Fibonacci number up till a limit

    :param limit: An integer

    :returns: A list containing all the fibonacci numbers < limit
    
    .. code-block:: python
    
        print(fib_till(100)) #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        print(sum(fib_till(1000))) #2583
        
    '''
    if type(limit) != int:
        return "limit must be an integer"
    fibnumbers = []
    n = 1
    while fibonacci(n) <= limit:
        fibnumbers.append(fibonacci(n))
        n += 1
    return fibnumbers

def zeckendorf_representation(x):
    '''
    Finds the `Zeckendorf Representation <https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem>`_ of x 

    :param x: An integer

    :returns: A list containing the zeckendorf representation of x
    
    .. code-block:: python
        
        print(zeckendorf_representation(64)) #[55, 8, 1]

    '''
    if type(x) != int:
        return "x must be an integer"
    zeckrep = []
    fibs = fib_till(x)[::-1]
    
    number = x
    count = 0
    while number != 0:
        if number - fibs[count] >= 0:
            number -= fibs[count]
            zeckrep.append(fibs[count])
            count += 1
        count += 1
    return zeckrep