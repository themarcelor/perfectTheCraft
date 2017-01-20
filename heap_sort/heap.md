# Heap Sort

Statement:
Given a disordered list of integers (or any other items),
rearrange the integers in natural order.

Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
Sample Output: [0,1,2,3,4,5,5,6,7,8,9]

Time Complexity of Solution:
Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n)).

Approach:
Heap sort happens in two phases. In the first phase, the array
is transformed into a heap. A heap is a binary tree where
1. each node is greater than each of its children
2. the tree is perfectly balanced
3. all leaves are in the leftmost position available.
In phase two the heap is continuously reduced to a sorted array:
1. while the heap is not empty
- remove the top of the head into an array
- fix the heap.
Heap sort was invented by John Williams not by B. R. Heap.

MoveDown:
The movedown method checks and verifies that the structure is a heap.

Technical Details:
A heap is based on an array just as a hashmap is based on an
array. For a heap, the children of an element n are at index
2n+1 for the left child and 2n+2 for the right child.

The movedown function checks that an element is greater than its
children. If not the values of element and child are swapped. The
function continues to check and swap until the element is at a
position where it is greater than its children.
