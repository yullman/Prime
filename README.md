#Свойство 1

для любого простого числа n>3 есть простое число n2<n, так, что n+n2 лежит на расстоянии 1 от простого числа


#Свойство 2

для любого простого числа n>5 существует два меньших простых числа n0,n1, такие что n0+n1 лежит на расстоянии 1 от n

из этого свойства так же вытекает, что максимальный промежуток между простым числом n и следующим простым числом не больше, чем n + прошлое простое число + 1

#ENG

#Property 1

For any prime n>3, there exists a smaller prime n2<n such that n+n2 is at distance 1 from a prime

#Property 2

For any prime n>5, there exist two smaller primes n0,n1 such that n0+n1 is at distance 1 from n

It also follows from this property that the maximum interval between a prime number n and the next prime number is no greater than n + the previous prime number + 1

#Data

PrimeDict.txt maps each prime n to the index of the smallest qualifying smaller prime (1 = immediately preceding prime, 2 = the one before that, etc.)

#Results

Both properties were tested on all primes up to 100,000.

Property 1: 9589 primes tested, 0 counterexamples.

Property 2: 9589 primes tested, 0 counterexamples.



