========
Overview
========

.. image:: https://img.shields.io/pypi/v/mathslib.svg
        :target: https://pypi.python.org/pypi/mathslib

.. image:: https://readthedocs.org/projects/mathslib/badge/?version=latest
        :target: https://mathslib.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

`mathslib`__ is a compilation of Mathematical Functions and Algorithms I have made or come across.
I have used most of these for `Project Euler`_.
 
See my website `ivl-projecteuler.com`_ for their implementation

See the full documentation `here`_

Breakdown
---------
+----------------+------------------------------------------------------------+
|numtheory.py    | * divisors_of(x, include_x)                                |
|                | * divisors(x, n)                                           |
|                | * continued_fraction(x)                                    |
|                | * overall_fraction(x)                                      |
|                | * phi(x)                                                   |
|                | * phi_sieve(x)                                             |
|                | * mobius(x)                                                |
|                | * mobius_k_sieve(limit, k)                                 |
|                | * count_k_free(n, k)                                       |
|                | * ppt(limit, non_primitive)                                |
|                | * k_smooth_numbers(max_prime, limit)                       |
|                | * k_powerful(k, limit, count)                              |
|                | * legendre_factorial(x)                                    |
|                | * tonelli_shanks(a, p)                                     |
|                | * ChineseRemainderTheorem(a1, a2, n1, n2)                  |
|                | * Generalised_CRT(a1, a2, n1, n2)                          |
|                | * FrobeniusNumber(\*integers)                              |
+----------------+------------------------------------------------------------+
|prime.py        | * prime_sieve(limit, block_size, segment, values)          |
|                | * is_prime(x)                                              |
|                | * prime_factors(x)                                         |
|                | * primepi(x)                                               |
|                | * sum_of_primes(x)                                         |
|                | * fermat_primality_test(x)                                 |
|                | * miller(n, millerrabin, numoftests)                       |
+----------------+------------------------------------------------------------+
|linalg.py       | * GaussJordanElimination(matrix, augmentedpart)            |
|                | * solve(M, b)                                              |
|                | * inverse(matrix)                                          |
|                | * determinant(matrix)                                      |
|                | * matrix_addition(A, B, subtract)                          |
|                | * identity(l, val)                                         |
|                | * concatenate(A, B)                                        |
|                | * argmax(alist)                                            |
|                | * fillmatrix(size, val)                                    |
|                | * matrix_mul(A, B)                                         |
+----------------+------------------------------------------------------------+
|fib.py          | * fibonacci(n)                                             |
|                | * fib_till(limit)                                          |
|                | * ZeckendorfRepresentation(x)                              |
+----------------+------------------------------------------------------------+
|algorithms.py   | * PrimsAlgorithm(matrix)                                   |
|                | * DijkstrasAlgorithm(graph, start_node, INFINITY)          |
|                | * FloydWarshallAlgorithm(graph, INFINITY)                  |
|                | * KnapSack(values, weights, n, W, no_values)               |
|                | * KnapSackValues(values, weights, n, W, no_values)         |
|                | * BFSSearch(g, start_node, end_node)                       |
|                | * DFSSearch(g, start_node, end_node)                       |
|                | * ConvexHullGiftWrapping(pts)                              |
|                | * ConvexHullDC(pts)                                        |
+----------------+------------------------------------------------------------+
|simple.py       | * n_choose_r(n, r)                                         | 
|                | * numberToBase(n, b)                                       |
|                | * ExtendedEuclideanAlgorithm(n, b)                         |
|                | * lcm(a_list)                                              |
|                | * ModDivision(a, b, m)                                     |
|                | * IsClockwise(a, b, c)                                     |
+----------------+------------------------------------------------------------+

.. _Project Euler: https://projecteuler.net
.. _ivl-projecteuler.com: https://ivl-projecteuler.com
.. _mathslib1: https://pypi.python.org/pypi/mathslib
.. _here: https://mathslib.readthedocs.io/en/latest/index.html
__ mathslib1_
