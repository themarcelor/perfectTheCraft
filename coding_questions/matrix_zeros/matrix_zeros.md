2D Matrix with -1

Given a bidimensional matrix comprised of random numbers and some "-1"s spread through it, find the "-1"s and set all the numbers in the same line and the same column to  zero (0).

* Example. Here is a 3x3 matrix with lines 0,1 and 2 and columns 0,1 and 2:

  | ... | *0* | *1* | *2* |
  | --- | --- | --- | --- |
  | *0* |  3  |  2  |  -1 |
  | *1* |  6  |  0  |  9  |
  | *2* |  2  |  6  |  -1 |

Based on the coordinates of the "-1"s found in this matrixs ( 0,2 and 2,2 ), lines 0 and 2 and column 2 must have all its elements replaced with zeros.

* This is the result:

  | ... | *0* | *1* | *2* |
  | --- | --- | --- | --- |
  | *0* |  0  |  0  |  0  |
  | *1* |  6  |  0  |  0  |
  | *2* |  0  |  0  |  0  |

