import random

array = [15, 6, 2, 12, 4]

def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp

#num_scans = 0
def find_smallest_num_idx(array, lower):
    smallestNumIdx = lower
    #global num_scans
    #num_scans +=1

    #lower+1 as it is pointless to check the first index against itself
    for idx in range(lower+1, len(array)):
        #print "scan # " + str(num_scans) + ": checking " + str(array[idx]) + " against " + str(array[smallestNumIdx])
        if array[idx] < array[smallestNumIdx]:
            smallestNumIdx = idx

    return smallestNumIdx

def selection_sort(array):
    print "unsorted: " + str(array)
    for idx in range(0,len(array)):
        to_be_swapped = find_smallest_num_idx(array,idx)
        if idx != to_be_swapped:
            swap(array,idx,to_be_swapped)
    print "sorted: " + str(array)

if __name__ == '__main__':
    #swap(array,0,2)
    #print find_smallest_num_idx(array,0)
    selection_sort(array)
