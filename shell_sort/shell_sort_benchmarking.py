import timeit

setup = '''
import random

array = [random.randint(0,100) for i in range(100)]


def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


def shell_sort(array):
    inc = 1
    while inc*2 < len(array):
        inc = inc * 2
    inc -= 1

    while inc >=1:
        for i in range(inc,len(array)):
            j = i
            while j > inc-1 and array[j] < array[j-inc]:
                swap(array, j, j-inc)
                j = j - inc
        inc = inc / 2
'''

print min(timeit.Timer('arr=array[:]; shell_sort(arr)', setup=setup).repeat(7, 1000))
