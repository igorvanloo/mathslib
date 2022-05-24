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
|                | * mobius(x)                                                |
|                | * ppt(limit, non_primitive)                                |
|                | * legendre_factorial(x)                                    |
|                | * tonelli_shanks(a, p)                                     |
|                | * ChineseRemainderTheorem(a1, a2, n1, n2)                  |
+----------------+------------------------------------------------------------+
|prime.py        | * prime_sieve(limit, block_size, segment, values)          |
|                | * is_prime(x)                                              |
|                | * prime_factors(x)                                         |
|                | * primepi(x)                                               |
|                | * sum_of_primes(x)                                         |
|                | * fermat_primality_test(x)                                 |
+----------------+------------------------------------------------------------+
|fib.py          | * fibonacci(n)                                             |
|                | * fib_till(limit)                                          |
|                | * ZeckendorfRepresentation(x)                              |
+----------------+------------------------------------------------------------+
|algorithms.py   | * PrimsAlgorithm(matrix)                                   |
|                | * DijkstrasAlgorithm(matrix, start_node, end_node)         |
|                | * KnapSack(values, weights, n, W, no_values)               |
|                | * KnapSackValues(values, weights, n, W, no_values)         |
+----------------+------------------------------------------------------------+
|simple.py       | * n_choose_r(n, r)                                         | 
|                | * numberToBase(n, b)                                       |
|                | * lcm(a_list)                                              |
|                | * ModDivision(a, b, m)                                     |
+----------------+------------------------------------------------------------+

.. _Project Euler: https://projecteuler.net
.. _ivl-projecteuler.com: https://ivl-projecteuler.com
.. _mathslib1: https://pypi.python.org/pypi/mathslib
.. _here: https://mathslib.readthedocs.io/en/latest/index.html
__ mathslib1_
