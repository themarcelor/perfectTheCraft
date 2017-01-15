# Merge Sort

Divide and conquer algorithm that needs additional O(N) of memory space.
It merges sorted arrays A and B into array C:

  * A = | 2 | 8 | 14 | 24 |
  * B = | 5 | 7 | 9 | 11 |

  * C = | *2* |  |  |  |  |  |  |  |


Brief set of steps:

1. Compare A[i] andB[j].

2. Copy the smaller value to C[K].

3. Increment the index of the array that was subject to iteration (in the example above, that'd be"A" => *C[0] = 2*).

4. Increment k.

5. Recursively repeat this "merge" process by continuously splitting the array into left and right partitions.


* Divide and Conquer

  * | 12 | 8 | 14 | 4 | 6 | 33 | 2 | 27 |
    * **Divide**
    * *split* | 12 | 8  | 14 | 4  |
	* *split* | 6  | 33 | 2  | 27 |
 	  * *split* | 12 | 8  |
  	  * *split* | 14 | 4  |
	  * *split* | 6  | 33 |
	  * *split* | 2  | 27 |
	* **Conquer**
    * *merge* | 4  | 8  | 12 | 14 |
	* *merge* | 2  | 6  | 27 | 33 |
  * **Combine**
  * *merge* | 2 | 4 | 6 | 8 | 12 | 14 | 27 | 33 |

#Output:
  * ```python
    meh
	```

# Emacs:
  *!(merge_emacs)[merge_emacs.jpg]
