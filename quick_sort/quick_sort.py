
array = [7, 15, 4, 9, 6, 18, 9, 12]


def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


def partition(array, first, last):
    print "working on partition: " + str(array[first:last+1])
    # pivot = the element in the middle
    pivot = array[(first + last)/2]
    #print "a new pivot has been defined: " + str(pivot)

    # The starting point for both must be OUTSIDE the array area
    # both pointers will move from left to right and right to left
    i = first-1
    j = last+1

    while True:
        i += 1
        j -= 1
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        # once both incrementing(i) and decrementing(j) loops stop
        # SWAP only if the left index is smaller than the right index
        # If the indexes cross each other, return j (it will be the last element of the "left array")
        if i < j:
            swap(array, i, j)
        else:
            return j


def quick_sort(array, first, last):
    split = partition(array, first, last)

    # if the starting point is smaller than the split
    # we are recursively applying quick_sort against the LEFT side
    #print "first: " + str(first) + " < split: " + str(split)
    if first < split:
        quick_sort(array, first, split)
    # if the last index of the sub-array from this recursion is greater than split+1
    # we are recursively applying quick_sort against the RIGHT side
    #print "last: " + str(last) + " < split+1: " + str(split+1)
    if last > split+1:
        quick_sort(array, split+1, last)

    # Determine when it circles through the last recusions's callback
    # i.e., back to the original set of args
    #if first == 0 and last == len(array)-1:
    #    print "finished"

if __name__ == '__main__':
    quick_sort(array, 0, len(array)-1)
    print array

