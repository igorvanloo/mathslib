.. highlight:: shell

=====
Usage
=====

In the python console you can import functions as you need them

.. code-block:: python3

    from mathslib import divisor
    div9 = divisor(2, 9)
    print(div9) #91
    
Otherwise you can import the whole module and use the mathslib. prefix

.. code-block:: python3

    import mathslib
    print(mathslib.tonelli_shanks(5, 41)) #28
    print(mathslib.ChineseRemainderTheorem(2, 3, 3, 5)) #8
    print(mathslib.ZeckendorfRepresentation(64)) #[55, 8, 1]


Example Solved Project Euler `problem 10 <https://projecteuler.net/problem=10>`_.
         
.. code-block:: python3
   
    from mathslib import sum_of_primes
    print(sum_of_primes(2*10**6)) #142913828922

