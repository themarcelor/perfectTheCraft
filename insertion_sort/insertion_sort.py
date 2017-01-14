import random

array = [15, 4, 2, 12, 6]


def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
                swap(array, j, j-1)
                j = j - 1
    print array

if __name__ == '__main__':
    insertion_sort(array)
