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

def n_choose_r(n, r): #nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))
    
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def lcm(a_list):
    n = sorted(a_list)
    curr = n.pop(-1)
    while len(n) != 0:
        temp = n.pop(-1)
        curr = int(abs(curr*temp)/math.gcd(curr, temp))
    return curr

def ModDivision(a, b, m):
    try:
        inv = pow(b, -1, m)
    except ValueError:
        if a % b == 0:
            answer = (a % m * b) // b
    else:
        a = a % m
        answer = (inv * a) % m
    return answer

