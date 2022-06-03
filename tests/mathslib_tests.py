'''
Test for all modules 

Author: Igor van Loo
'''

import unittest

import mathslib.primes as P
import mathslib.numtheory as NT
import mathslib.algorithms as ALGO
import mathslib.fib as FIB
import mathslib.simple as S

class TestNumberTheory(unittest.TestCase):
    
    def test_divisors_of(self):
        self.assertEqual(NT.divisors_of(15), [1, 3, 5, 15])
        self.assertEqual(NT.divisors_of(15, include_x = False), [1, 3, 5])
        
    def test_divisor(self):
        self.assertEqual(NT.divisor(0, 9), 3)
        self.assertEqual(NT.divisor(1, 9), 13)
        self.assertEqual(NT.divisor(2, 9), 91)
    
    def test_continued_fraction(self):
        self.assertEqual(NT.continued_fraction(19), [4, 2, 1, 3, 1, 2, 8])
        
    def test_overall_fraction(self):
        self.assertEqual(NT.overall_fraction([4, 2, 6, 7]), (415, 93))
    
    def test_phi(self):
        self.assertEqual(NT.phi(20), 8)
        self.assertEqual(NT.phi(100), 40)
        
    def test_mobius(self):
        self.assertEqual(NT.mobius(10), 1)
        self.assertEqual(NT.mobius(9), 0)
        self.assertEqual(NT.mobius(7), -1)
        
    def test_ppt(self):
        self.assertEqual(NT.ppt(20), [[3, 4, 5], [6, 8, 10], [9, 12, 15], [12, 16, 20], [5, 12, 13], [15, 8, 17]])
        self.assertEqual(NT.ppt(20, False), [[3, 4, 5], [5, 12, 13], [15, 8, 17]])
        self.assertEqual(len(NT.ppt(100, False)), 16)
        
    def test_legendre_factorial(self):
        self.assertEqual(NT.legendre_factorial(6), {2: 4, 3: 2, 5: 1})
        self.assertEqual(NT.legendre_factorial(10), {2: 8, 3: 4, 5: 2, 7: 1})
        
    def test_k_smooth_numbers(self):
        self.assertEqual(len(NT.k_smooth_numbers(5, 10**8)), 1105)
    
    def test_legendre_symbol(self):
        self.assertEqual(NT.legendre_symbol(3, 3), 0)
        self.assertEqual(NT.legendre_symbol(10, 31), 1)
        self.assertEqual(NT.legendre_symbol(2, 11), -1)
        
    def test_tonelli_shanks(self):
        self.assertEqual(NT.tonelli_shanks(5, 41), 28)
        
    def test_chinese_remainder_theorem(self):
        self.assertEqual(NT.ChineseRemainderTheorem(2, 3, 3, 5), 8)
        self.assertEqual(NT.ChineseRemainderTheorem(8, 2, 15, 7), 23)
    
    def test_frobenius_number(self):
        self.assertEqual(NT.FrobeniusNumber(3, 5), 7)
        self.assertEqual(NT.FrobeniusNumber(6, 9, 20), 43)
        self.assertEqual(NT.FrobeniusNumber(1000, 1476, 3764, 4864, 4871, 7773), 47350)

class TestPrimes(unittest.TestCase):
    
    def test_prime_sieve(self):
        test_prime = P.prime_sieve(100)
        self.assertEqual(len(test_prime), 25)
        self.assertEqual(test_prime[-1], 97)
        test_prime2 = P.prime_sieve(10, values = False)
        self.assertEqual(test_prime2, [False, False, True, True, False, True, False, True, False, False, False])
    
    def test_is_prime(self):
        self.assertEqual(P.is_prime(10), False)
        self.assertEqual(P.is_prime(160517089),True)
        
    def test_prime_factors(self):
        self.assertEqual(P.prime_factors(123123), {3: 1, 7: 1, 11: 1, 13: 1, 41: 1})
        self.assertEqual(P.prime_factors(1123619623), {7: 1, 160517089: 1})
        
    def test_primepi(self):
        self.assertEqual(P.primepi(10), [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4])
        
    def test_sum_of_primes(self):
        self.assertEqual(P.sum_of_primes(2*10**6), 142913828922)
        self.assertEqual(P.sum_of_primes(10**8), 279209790387276)
    
    def test_fermat_primality_test(self):
        self.assertEqual(P.fermat_primality_test(17969800575241), True)
        self.assertEqual(P.fermat_primality_test(101101), True)
        self.assertEqual(P.fermat_primality_test(101101, 6), False)
        self.assertEqual(P.fermat_primality_test(3), True)
        
    def test_miller_primality_test(self):
        self.assertEqual(P.miller(17969800575241), True)
        self.assertEqual(P.miller(101101), False)
        self.assertEqual(len([x for x in range(1, 10**5) if P.miller(x, True, 1)]), 9608)
        self.assertEqual(len([x for x in range(1, 10**5) if P.miller(x, True, 2)]), 9592)
        
class TestSimple(unittest.TestCase):
    
    def test_n_choose_r(self):
        self.assertEqual(S.n_choose_r(50, 30), 47129212243960)
        
    def test_numbertobase(self):
        self.assertEqual(S.numberToBase(10, 2), [1, 0, 1, 0])
        self.assertEqual(S.numberToBase(10, 3), [1, 0, 1])
    
    def test_lcm(self):
        self.assertEqual(S.lcm([2,3]), 6)
        self.assertEqual(S.lcm([8345, 23579, 174]), 34237415370)
        
    def test_mod_division(self):
        self.assertEqual(S.ModDivision(8, 4, 5), 2)
        
class TestFib(unittest.TestCase):
    
    def test_fibonacci(self):
        self.assertEqual(FIB.fibonacci(100), 354224848179261915075)
        
    def test_fibtill(self):
        self.assertEqual(FIB.fib_till(100)[-1], 89)
        self.assertEqual(sum(FIB.fib_till(1000)), 2583)
    
    def test_zeckendorf(self):
        self.assertEqual(FIB.ZeckendorfRepresentation(64), [55, 8, 1])

class TestAlgorithms(unittest.TestCase):
    
    def test_Prims(self):
        matrix = [[0, 16, 12, 21, 0, 0, 0], 
                  [16, 0, 0, 17, 20, 0, 0], 
                  [12, 0, 0, 28, 0, 31, 0], 
                  [21, 17, 28, 0, 18, 19, 23], 
                  [0, 20, 0, 18, 0, 0, 11], 
                  [0, 0, 31, 19, 0, 0, 27], 
                  [0, 0, 0, 23, 11, 27, 0]]
        self.assertEqual(ALGO.PrimsAlgorithm(matrix), (93, 
                                  [[0, 16, 12, 0, 0, 0, 0],
                                   [16, 0, 0, 17, 0, 0, 0],
                                   [12, 0, 0, 0, 0, 0, 0],
                                   [0, 17, 0, 0, 18, 19, 0],
                                   [0, 0, 0, 18, 0, 0, 11],
                                   [0, 0, 0, 19, 0, 0, 0],
                                   [0, 0, 0, 0, 11, 0, 0]]))
    
    def test_Dijkstras(self):
        matrix = [[131, 673, 234, 103,18],
                 [201, 96, 342, 965, 150],
                 [630, 803, 746, 422, 111],
                 [537, 699, 497, 121, 956],
                 [805, 732, 524, 37, 331]]
        self.assertEqual(ALGO.DijkstrasAlgorithm(matrix), 2297)
    
    def test_KnapSack(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        n = len(values)
        
        self.assertEqual(ALGO.KnapSack(values, weights, n, W), 220)
    
    def test_KnapSackValues(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        n = len(values)
        
        self.assertEqual(ALGO.KnapSackValues(values, weights, n, W), {20, 30})

if __name__ == "__main__":
    unittest.main()