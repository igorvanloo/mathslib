'''
Test for all modules 

Author: Igor van Loo
'''

import unittest

import mathslib.numtheory as NT
import mathslib.primes as P
import mathslib.divisors as DIV
import mathslib.linalg as LA
import mathslib.fib as FIB
import mathslib.algorithms as ALGO
import mathslib.simple as S

class TestNumberTheory(unittest.TestCase):
    
    def test_phi(self):
        self.assertEqual(NT.phi(20), 8)
        self.assertEqual(NT.phi(100), 40)
    
    def test_phi_sieve(self):
        self.assertEqual(NT.phi_sieve(10), [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4])
        self.assertEqual(NT.phi_sieve(20)[11:], [10, 4, 12, 6, 8, 8, 16, 6, 18, 8])
        
    def test_phi_sum(self):
        self.assertEqual(NT.phi_sum(10**7), 30396356427242)
        self.assertEqual(NT.phi_sum(10**4), sum(NT.phi_sieve(10**4)))
        self.assertEqual(NT.phi_sum(10**4), sum(NT.phi(i) for i in range(1, 10**4 + 1)))
        
    def test_mobius(self):
        self.assertEqual(NT.mobius(10), 1)
        self.assertEqual(NT.mobius(9), 0)
        self.assertEqual(NT.mobius(7), -1)
    
    def test_mobius_k_sieve(self):
        self.assertEqual(NT.mobius_k_sieve(10), [0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1])
        self.assertEqual(NT.mobius_k_sieve(10, 3), [0, 1, -1, -1, -1, -1, 1, -1, 0, -1, 1])
    
    def test_count_k_free(self):
        self.assertEqual(NT.count_k_free(1000, 2), 608)
        self.assertEqual(NT.count_k_free(1000, 3), 832)
        
    def test_pythagoren_triples(self):
        self.assertEqual(NT.pythagorean_triples(20), [[3, 4, 5], [6, 8, 10], [9, 12, 15], [12, 16, 20], [5, 12, 13], [15, 8, 17]])
        self.assertEqual(NT.pythagorean_triples(20, False), [[3, 4, 5], [5, 12, 13], [15, 8, 17]])
        self.assertEqual(len(NT.pythagorean_triples(100, False)), 16)
    
    def test_count_primitive_pythagorean_triples(self):
        self.assertEqual(NT.count_primitive_pythagorean_triples(10**10), 1591549475)
        self.assertEqual(NT.count_primitive_pythagorean_triples(10**8), 15915493)
        
    def test_legendre_factorial(self):
        self.assertEqual(NT.legendre_factorial(6), {2: 4, 3: 2, 5: 1})
        self.assertEqual(NT.legendre_factorial(10), {2: 8, 3: 4, 5: 2, 7: 1})
        
    def test_k_smooth_numbers(self):
        self.assertEqual(len(NT.k_smooth_numbers(5, 10**8)), 1105)
        
    def test_k_powerful(self):
        self.assertEqual(NT.k_powerful(2, 10**2), 14)
        self.assertEqual(NT.k_powerful(2, 10**2, False), [1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 72, 81, 100])
    
    def test_legendre_symbol(self):
        self.assertEqual(NT.legendre_symbol(3, 3), 0)
        self.assertEqual(NT.legendre_symbol(10, 31), 1)
        self.assertEqual(NT.legendre_symbol(2, 11), -1)
        
    def test_tonelli_shanks(self):
        self.assertEqual(NT.tonelli_shanks(5, 41), 28)
        
    def test_chinese_remainder_theorem(self):
        self.assertEqual(NT.chinese_remainder_theorem(2, 3, 3, 5), 8)
        self.assertEqual(NT.chinese_remainder_theorem(8, 2, 15, 7), 23)
        
    def test_generalised_crt(self):
        self.assertEqual(NT.generalised_CRT(2, 3, 3, 5), 8)
        self.assertEqual(NT.generalised_CRT(2, 4, 4, 6), 10)
        self.assertEqual(NT.generalised_CRT(3, 4, 4, 6), 'No solution')
        
    def test_frobenius_number(self):
        self.assertEqual(NT.frobenius_number(3, 5), 7)
        self.assertEqual(NT.frobenius_number(6, 9, 20), 43)
        self.assertEqual(NT.frobenius_number(1000, 1476, 3764, 4864, 4871, 7773), 47350)
    
    def test_continued_fraction(self):
        self.assertEqual(NT.continued_fraction(19), [4, 2, 1, 3, 1, 2, 8])
        
    def test_overall_fraction(self):
        self.assertEqual(NT.overall_fraction([4, 2, 6, 7]), (415, 93))

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
        
    def test_spf_sieve(self):
        self.assertEqual(P.spf_sieve(10), [0, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2])
    
    def test_primepi(self):
        self.assertEqual(P.primepi(10**6), 78498)
        self.assertEqual(P.primepi(10**7), 664579)
        self.assertEqual(P.primepi(10**8), 5761455)
        self.assertEqual(P.primepi(10**9), 50847534)
        
    def test_primepi_sieve(self):
        self.assertEqual(P.primepi_sieve(10), [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4])
        
    def test_sum_of_primes(self):
        self.assertEqual(P.sum_of_primes(2*10**6), 142913828922)
        self.assertEqual(P.sum_of_primes(10**8), 279209790387276)
    
    def test_fermat_primality_test(self):
        self.assertEqual(P.fermat_primality_test(17969800575241), True)
        self.assertEqual(P.fermat_primality_test(101101), True)
        self.assertEqual(P.fermat_primality_test(101101, 6), False)
        self.assertEqual(P.fermat_primality_test(3), True)
        
    def test_miller_primality_test(self):
        self.assertEqual(P.miller_primality_test(17969800575241), True)
        self.assertEqual(P.miller_primality_test(101101), False)
        self.assertEqual(len([x for x in range(1, 10**5) if P.miller_primality_test(x, True, 1)]), 9608)
        self.assertEqual(len([x for x in range(1, 10**5) if P.miller_primality_test(x, True, 2)]), 9592)

class TestDivisors(unittest.TestCase):
    
    def test_divisors_of(self):
        self.assertEqual(DIV.divisors(15), [1, 3, 5, 15])
        self.assertEqual(DIV.divisors(15, proper = True), [1, 3, 5])
        
    def test_divisor(self):
        self.assertEqual(DIV.divisor(0, 9), 3)
        self.assertEqual(DIV.divisor(1, 9), 13)
        self.assertEqual(DIV.divisor(2, 9), 91)
    
    def test_divisor_sieve(self):
        self.assertEqual(DIV.divisor_sieve(0, 10), [0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4])
        self.assertEqual(DIV.divisor_sieve(1, 10), [0, 1, 3, 4, 7, 6, 12, 8, 15, 13, 18])
        self.assertEqual(DIV.divisor_sieve(2, 10), [0, 1, 5, 10, 21, 26, 50, 50, 85, 91, 130])
        
class TestLinearAlgebra(unittest.TestCase):
    
    def test_GaussJordanElimination(self):
        matrix = [[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]]
        self.assertEqual(LA.gauss_jordan_elimination(matrix), True)
    
    def test_solve(self):
        matrix = [[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]]
        b = [[8],
             [-11],
             [-3]]
        self.assertEqual(LA.solve(matrix, b), [[2.0], [3.0], [-1.0]])
    
    def test_inverse(self):
        matrix = [[1, -1, 0], 
                  [-8, 9, -1], 
                  [-9, 0, 10]]
        self.assertEqual(LA.inverse(matrix), [[90.0, 10.0, 1.0], [89.0, 10.0, 1.0], [81.0, 9.0, 1.0]])
    
    def test_determinant(self):
        matrix = [[7, -1, 0], 
                  [-8, 9, -1], 
                  [-9, 0, 10]]
        self.assertEqual(LA.determinant(matrix), 541.0)
        
    def test_matrix_addition(self):
        matrix = [[1, 0, 0], 
                  [0, 1, 0], 
                  [0, 0, 1]]
        self.assertEqual(LA.matrix_addition(matrix, matrix), [[2, 0, 0], [0, 2, 0], [0, 0, 2]])
        self.assertEqual(LA.matrix_addition(matrix, matrix, True), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    
    def test_identity(self):
        self.assertEqual(LA.identity(2), [[1, 0], [0, 1]])
        self.assertEqual(LA.identity(2, 5), [[5, 0], [0, 5]])
    
    def test_concatenate_matrix(self):
        A = [[1, 0],
             [0, 1]]
        self.assertEqual(LA.concatenate(A, A), [[1, 0, 1, 0], [0, 1, 0, 1]])
        
    def test_argmax(self):
        self.assertEqual(LA.argmax([1, 3, 2]), 1)
        
    def test_fillmatrix(self):
        self.assertEqual(LA.fillmatrix((2, 2)), [[0, 0], [0, 0]])
        self.assertEqual(LA.fillmatrix((2, 3)), [[0, 0, 0], [0, 0, 0]])
    
    def test_matrixmul(self):
        A = [[2, 0], 
             [0, 2]]
        B = [[1, 2], 
             [3, 1]]
        self.assertEqual(LA.matrix_mul(A, B), [[2, 4], [6, 2]])
    
    def test_matrix_pow(self):
        A = [[1, 1], 
             [1, 0]]
        self.assertEqual(LA.matrix_pow(A, 10), [[89, 55], [55, 34]])

class TestFib(unittest.TestCase):
    
    def test_fibonacci(self):
        self.assertEqual(FIB.fibonacci(100), 354224848179261915075)
        self.assertEqual(FIB.fibonacci(100, 10**7 + 9), 5475613)
        
    def test_fibtill(self):
        self.assertEqual(FIB.fib_till(100)[-1], 89)
        self.assertEqual(sum(FIB.fib_till(1000)), 2583)
    
    def test_zeckendorf(self):
        self.assertEqual(FIB.zeckendorf_representation(64), [55, 8, 1])
        
class TestAlgorithms(unittest.TestCase):
    
    def test_Prims(self):
        matrix = [[0, 16, 12, 21, 0, 0, 0], 
                  [16, 0, 0, 17, 20, 0, 0], 
                  [12, 0, 0, 28, 0, 31, 0], 
                  [21, 17, 28, 0, 18, 19, 23], 
                  [0, 20, 0, 18, 0, 0, 11], 
                  [0, 0, 31, 19, 0, 0, 27], 
                  [0, 0, 0, 23, 11, 27, 0]]
        self.assertEqual(ALGO.prims_algorithm(matrix), (93, 
                                  [[0, 16, 12, 0, 0, 0, 0],
                                   [16, 0, 0, 17, 0, 0, 0],
                                   [12, 0, 0, 0, 0, 0, 0],
                                   [0, 17, 0, 0, 18, 19, 0],
                                   [0, 0, 0, 18, 0, 0, 11],
                                   [0, 0, 0, 19, 0, 0, 0],
                                   [0, 0, 0, 0, 11, 0, 0]]))
    
    def test_Dijkstras(self):
        g = [[[1, 7], [2, 9], [5, 14]],
             [[0, 7], [2, 10], [3, 15]],
             [[0, 9], [1, 10], [3, 11], [5, 2]],
             [[1, 15], [2, 11], [4, 6]],
             [[3, 6], [5, 9]],
             [[0, 14], [2, 2], [4, 9]]
            ]
        
        self.assertEqual(ALGO.dijkstras_algorithm(g), [0, 7, 9, 20, 20, 11])
    
    def test_FloydWarshall(self):
        g = [[[1, 7], [2, 9], [5, 14]],
             [[0, 7], [2, 10], [3, 15]],
             [[0, 9], [1, 10], [3, 11], [5, 2]],
             [[1, 15], [2, 11], [4, 6]],
             [[3, 6], [5, 9]],
             [[0, 14], [2, 2], [4, 9]]
            ]
        
        self.assertEqual(ALGO.floyd_warshall_algorithm(g), [[0, 7, 9, 20, 20, 11],
                                                          [7, 0, 10, 15, 21, 12],
                                                          [9, 10, 0, 11, 11, 2],
                                                          [20, 15, 11, 0, 6, 13],
                                                          [20, 21, 11, 6, 0, 9],
                                                          [11, 12, 2, 13, 9, 0]])
    def test_KnapSack(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        n = len(values)
        
        self.assertEqual(ALGO.knap_sack(values, weights, n, W), 220)
    
    def test_KnapSackValues(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        n = len(values)
        
        self.assertEqual(ALGO.knap_sack_values(values, weights, n, W), {20, 30})
    
    def test_BFSSearch(self):
        G = [[4, 1], [0, 5], [6, 3], [2, 7],
             [0, 8], [1, 6], [2, 5, 10], [3, 11],
             [4, 9], [8, 13], [6], [7, 15],
             [13], [9, 12, 14], [13, 15], [11, 14] ]
        self.assertEqual(ALGO.BFS(G), [0, 4, 8, 9, 13, 14, 15])
        
    def test_DFSSearch(self):
        G = [[4, 1], [0, 5], [6, 3], [2, 7],
             [0, 8], [1, 6], [2, 5, 10], [3, 11],
             [4, 9], [8, 13], [6], [7, 15],
             [13], [9, 12, 14], [13, 15], [11, 14] ]
        self.assertEqual(ALGO.DFS(G), [0, 1, 5, 6, 2, 3, 7, 11, 15])

class TestSimple(unittest.TestCase):
    
    def test_bin_exp(self):
        x = S.bin_exp(1/2, 1/2, 5, 10)  
        y = S.bin_exp(1/2, -1/2, 5, 10)
        self.assertEqual(x[1] - y[1], 55.0)
        
    def test_numbertobase(self):
        self.assertEqual(S.number_to_base(10, 2), [1, 0, 1, 0])
        self.assertEqual(S.number_to_base(10, 3), [1, 0, 1])
    
    def test_ExtendedEuclideanAlgorithm(self):
        self.assertEqual(S.extended_euclidean_algorithm(240, 46), (2, -9, 47))
        
    def test_lcm(self):
        self.assertEqual(S.lcm([2,3]), 6)
        self.assertEqual(S.lcm([8345, 23579, 174]), 34237415370)
        
    def test_mod_division(self):
        self.assertEqual(S.mod_division(8, 4, 5), 2)
        
    def test_bisect(self):
        self.assertEqual(S.bisect([2,3,5,7], 6), 3)
        
if __name__ == "__main__":
    unittest.main()