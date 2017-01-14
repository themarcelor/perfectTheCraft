array= [28,24,27,18]

def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


def bubble_sort(array):
    for i in range(len(array),1,-1):
        for j in range(0,i-1):
            if array[j] > array[j+1]:
                swap(array, j , j+1)
        print array

if __name__ == '__main__':
    bubble_sort(array)
