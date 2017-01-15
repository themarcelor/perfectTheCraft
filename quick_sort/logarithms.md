# A Quick Review of Logarithms

* log<sub>b</sub>n = the exponent to which b must be raised to get to n

  * log<sub>b</sub>n=x     if     b<sup>x</sup>=n
  
  * examples:
    * log<sub>2</sub>8 = 3 because 2<sup>3</sup> = 8
    * log<sub>10</sub>10000 = 4 because 10<sup>4</sup> = 10000


* In other words:
  * log<sub>b</sub>n is an upper bound on the number of divisions needed to reach 1.
  * e.g.: log<sub>2</sub>18 = 4.17
    18/2 = 9    9/2 = 4    4/2 = 2    2/2 = 1

* Algorithms that take O(log n), also known as logarithmic, are faster than the ones that operate in O(N), aka: Linear.
  Algorithms that take O(n*log n), also known as linearithimic, are faster than the ones that operation in O(N<sup>2</sup>), aka: Quadratic.


* Comparing the growth pattern of n and log<sub>2</sub>n:

  | n         | log<sub>2</sub>n |
  |-----------|------------------|
  | 2         | 1                |
  | 1024      | 10               |
  | 1024*1024 | 20               |


