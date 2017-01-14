# Bubble Sort

One of the worst algorithms.

Brief set of steps:

1. Compare in pairs (starting from the left).
2. Focus on the inner loop first:
   ```python
   for j in range(0, i-1)
   ```
   * Comparing in pairs: 
   ```python
   array[j] < array[j + 1]
   ```
3. Largest numbers bubble-up to the right. Whatever ends up on the far right is already sorted so the outer loop narrows down the sorting scope:
   ```python
   for i in range(len(array), 1, -1)
   ```

What did we learn here?
* Bubble sort does not focus on one item to perform a round of comparisons, it compares and swaps in pairs. That can lead to a high number of swaps.
* Move comparison bubbles forward while decrementing the limit indicator ( the “i” from the outer loop ).


# Output:

 ```python
 python bubble_sort.py 
 4.53432893753
 ```

# Emacs:
 ![bubble_emacs](bubble_sort.jpg)


