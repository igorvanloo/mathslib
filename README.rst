========
Overview
========

.. image:: https://img.shields.io/pypi/v/mathslib.svg
        :target: https://pypi.python.org/pypi/mathslib

.. image:: https://readthedocs.org/projects/mathslib/badge/?version=latest
        :target: https://mathslib.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

`mathslib`__ is a compilation of Mathematical Functions and Algorithms. Unless credit was given all
of the functions were written by me. Relevant articles are also linked where the implementation is complex.

I have used most of these for `Project Euler`_.
 
See my website `ivl-projecteuler.com`_ for their implementation

See the full documentation `here`_

Breakdown
---------
+----------------+------------------------------------------------------------+
|numtheory.py    | * phi(x)                                                   |
|                | * phi_sieve(x)                                             |
|                | * phi_sum(x)                                               |
|                | * mobius(x)                                                |
|                | * mobius_k_sieve(limit, k)                                 |
|                | * count_k_free(n, k)                                       |
|                | * pythagorean_triples(limit, non_primitive)                |
|                | * count_primitive_pythagorean_triples(n)                   |
|                | * k_smooth_numbers(max_prime, limit)                       |
|                | * k_powerful(k, limit, count)                              |
|                | * legendre_factorial(x)                                    |
|                | * tonelli_shanks(a, p)                                     |
|                | * chinese_remainder_theorem(a1, a2, n1, n2)                |
|                | * generalised_CRT(a1, a2, n1, n2)                          |
|                | * frobenius_number(\*integers)                             |
|                | * continued_fraction(x)                                    |
|                | * overall_fraction(x)                                      |
|                | * partition(x, L, show)                                    |
+----------------+------------------------------------------------------------+
|primes.py       | * prime_sieve(limit, block_size, segment, values)          |
|                | * prime_sieve_in_range(low_limit, upp_limit, values)       |
|                | * is_prime(x)                                              |
|                | * prime_factors(x)                                         |
|                | * spf_sieve(x)                                             |
|                | * primepi(x)                                               |
|                | * primepi_sieve(x)                                         |
|                | * sum_of_primes(x)                                         |
|                | * fermat_primality_test(x)                                 |
|                | * miller_primality_test(n, millerrabin, numoftests)        |
+----------------+------------------------------------------------------------+
|divisors.py     | * divisors(x, proper)                                      |
|                | * divisor(x, n)                                            |
|                | * divisor_sieve(x, n)                                      |
+----------------+------------------------------------------------------------+
|linalg.py       | * gauss_jordan_elimination(matrix, augmentedpart)          |
|                | * solve(M, b)                                              |
|                | * inverse(matrix)                                          |
|                | * determinant(matrix)                                      |
|                | * matrix_addition(A, B, subtract)                          |
|                | * identity(l, val)                                         |
|                | * concatenate(A, B)                                        |
|                | * argmax(alist)                                            |
|                | * fillmatrix(size, val)                                    |
|                | * matrix_mul(A, B)                                         |
|                | * matrix_pow(A, n)                                         |
+----------------+------------------------------------------------------------+
|fib.py          | * fibonacci(n, m)                                          |
|                | * fib_till(limit)                                          |
|                | * zeckendorf_representation(x)                             |
+----------------+------------------------------------------------------------+
|algorithms.py   | * prims_algorithm(matrix)                                  |
|                | * dijkstras_algorithm(graph, start_node, INFINITY)         |
|                | * floyd_warshall_algorithm(graph, INFINITY)                |
|                | * knap_sack(values, weights, n, W, no_values)              |
|                | * knap_sack_values(values, weights, n, W, no_values)       |
|                | * BFS(g, start_node, end_node)                             |
|                | * DFS(g, start_node, end_node)                             |
|                | * convex_hull_gift_wrapping(pts)                           |
|                | * convex_hull_DC(pts)                                      |
+----------------+------------------------------------------------------------+
|gaussianint.py  | * GI                                                       |
|                |  * conj(self)                                              |
|                |  * norm_sq(self)                                           |
|                |  * prime_fac(self)                                         |
|                | * rem(x, y)                                                |
|                | * gcd(x, y)                                                |
+----------------+------------------------------------------------------------+
|simple.py       | * bin_exp(a, b, c, n, m)                                   | 
|                | * number_to_base(n, b)                                     |
|                | * extended_euclidean_algorithm(n, b)                       |
|                | * lcm(a_list)                                              |
|                | * mod_division(a, b, m)                                    |
|                | * binom(n, k, p)                                           |
|                | * bisect(alist, goal)                                      |
|                | * is_clockwise(a, b, c)                                    |
+----------------+------------------------------------------------------------+

.. _Project Euler: https://projecteuler.net
.. _ivl-projecteuler.com: https://ivl-projecteuler.com
.. _mathslib1: https://pypi.python.org/pypi/mathslib
.. _here: https://mathslib.readthedocs.io/en/latest/index.html
__ mathslib1_
