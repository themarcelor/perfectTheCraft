# Insertion Sort

Brief set of steps:
1. Start moving through the items in the array ( to_insert = i )
2. Compare with all previous items ( i-1, i-2, i-3, … , i-n ) until it reaches the beginning of the array
3. Swap when necessary ( insert smallest numbers on the left side of the array )


What did we learn here?
* Insertion sort sucks.
* It is nice to keep this “reverse iteration” technique in mind ( for i in range(n, 0 , -1) ). Might come in handy later on.

# Output:

```python
python insertion_sort_benchmarking.py
2.20469784737
```
*The version with the while loop is slightly faster than the one with nested for's*


