import timeit
#array= [28,24,27,18]

setup = '''
import random

array = [random.randint(0,100) for i in range(100)]

def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


def bubble_sort(array):
    for i in range(len(array),1,-1):
        for j in range(0,i-1):
            if array[j] > array[j+1]:
                swap(array, j , j+1)
        #print array

#if __name__ == '__main__':
#    bubble_sort(array)
'''

print min(timeit.Timer('arr=array[:]; bubble_sort(arr)', setup=setup).repeat(7, 1000))
