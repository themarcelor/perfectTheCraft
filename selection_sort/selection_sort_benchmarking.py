import timeit

setup = '''
import random

array = [random.randint(0,100) for i in range(100)]

def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp

def find_smallest_num_idx(array, lower):
    smallestNumIdx = lower

    for idx in range(lower+1, len(array)):
        if array[idx] < array[smallestNumIdx]:
            smallestNumIdx = idx

    return smallestNumIdx

def selection_sort(array):
    for idx in range(0,len(array)):
        to_be_swapped = find_smallest_num_idx(array,idx)
        if idx != to_be_swapped:
            swap(array,idx,to_be_swapped)
'''

print min(timeit.Timer('arr=array[:]; selection_sort(arr)', setup=setup).repeat(7, 1000))
