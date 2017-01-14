#import pdb

array = [36,18,10,27,3,20,9,8]


def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


def shell_sort(array):
    inc = 1
    while inc*2 < len(array):
        inc = inc * 2
    inc -= 1
    #print "inc: " + str(inc)

    while inc >=1:
        #pdb.set_trace()
        for i in range(inc,len(array)):
            j = i
            #print "comparing " + str(array[j]) + " with " + str(array[j-inc])
            while j > inc-1 and array[j] < array[j-inc]:
                swap(array, j, j-inc)
                j = j - inc
                #print "swap! " + str(array)
        inc = inc / 2
    print array


if __name__ == '__main__':
    shell_sort(array)
