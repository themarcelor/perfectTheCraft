import timeit

setup = '''
import random

array = [random.randint(0,100) for i in range(100)]

def merge(array, temp_array, leftstart, leftend, rightstart, rightend):
    i = leftstart
    j = rightstart
    k = leftstart

    while i <= leftend and j <= rightend:
        if array[i] < array[j]:
            temp_array[k] = array[i]
            i=i+1
        else:
            temp_array[k] = array[j]
            j=j+1
        k=k+1

    while i <= leftend:
        temp_array[k] = array[i]
        i=i+1
        k=k+1

    while j <= rightend:
        temp_array[k] = array[j]
        j=j+1
        k=k+1

    for i in range(leftstart, rightend+1):
        array[i] = temp_array[i]


def merge_sort(array, temp_array, start, end):
    split_point = (start+end)/2

    if (end - start) > 0:
        merge_sort(array, temp_array, start, split_point)
        merge_sort(array, temp_array, split_point+1, end)
        merge(array, temp_array, start, split_point, split_point+1, end)
'''

print min(timeit.Timer('arr=array[:]; temp_array=array[:]; merge_sort(arr, temp_array, 0 , len(array)-1)', setup=setup).repeat(7, 1000))
