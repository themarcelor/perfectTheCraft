import timeit

setup = '''
import random

array = [random.randint(0,100) for i in range(100)]

def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp

#def insertion_sort(array):
#    for i in range(1,len(array)):
#        for j in range(i,0,-1):
#            if array[j] < array[j-1]:
#                swap(array, j, j-1)
#    #print array

def insertion_sort(array):
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
                swap(array, j, j-1)
                j = j - 1
    #print array
'''

print min(timeit.Timer('arr=array[:]; insertion_sort(arr)', setup=setup).repeat(7, 1000))
