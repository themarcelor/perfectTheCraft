import timeit

setup = '''
import random

array = [random.randint(0,100) for i in range(100)]

def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


def partition(array, first, last):
    # pivot = the element in the middle
    pivot = array[(first + last)/2]
    i = first-1
    j = last+1

    while True:
        i += 1
        j -= 1
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i < j:
            swap(array, i, j)
        else:
            return j


def quick_sort(array, first, last):
    split = partition(array, first, last)

    if first < split:
        quick_sort(array, first, split)
    if last > split+1:
        quick_sort(array, split+1, last)
'''

print min(timeit.Timer('arr=array[:]; quick_sort(arr, 0 , 99)', setup=setup).repeat(7, 1000))
