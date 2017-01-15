import pdb

array = [8, 12, 4, 14, 6, 33, 2, 27]


def merge(array, temp_array, leftstart, leftend, rightstart, rightend):
    print "working with array A: " + str(array[leftstart:leftend+1]) + " and array B: " + str(array[rightstart:rightend+1])
    i = leftstart
    j = rightstart
    k = leftstart

    while i <= leftend and j <= rightend:
        #print "comparing i: " + str(array[i]) + " with j: " + str(array[j])
        if array[i] < array[j]:
            temp_array[k] = array[i]
            print "_ temp_array -> insert i: " + str(temp_array)
            i=i+1
        else:
            temp_array[k] = array[j]
            print "_ temp_array -> insert j: " + str(temp_array)
            j=j+1
        k=k+1

    #pdb.set_trace()
    #print "i: " + str(i) + " less than leftend: " + str(leftend)
    while i <= leftend:
        temp_array[k] = array[i]
        i=i+1
        k=k+1
        #print "__ temp_array: " + str(temp_array)

    while j <= rightend:
        temp_array[k] = array[j]
        j=j+1
        k=k+1
        #print "___ temp_array: " + str(temp_array)

    # set range from the beginning of the left array to the end of the right array +1
    # (Python needs this +1 so it will increment all the way to the last element of the array)
    for i in range(leftstart, rightend+1):
        array[i] = temp_array[i]


def split_array(array, temp_array, start, end):
    #print "_____ temp_array: " + str(temp_array)
    #print "start: " + str(start)
    #print "end: " + str(end)
    split_point = (start+end)/2

    if (end - start) > 0:
        #print "array A: " + str(array[start:split_point+1])
        split_array(array, temp_array, start, split_point)
        #print "array B: " + str(array[split_point+1:end+1])
        split_array(array, temp_array, split_point+1, end)
        merge(array, temp_array, start, split_point, split_point+1, end)


if __name__ == '__main__':
    # temporary array with zeroes helps visualize the first allocation of numbers
    temp_array = [0, 0, 0, 0, 0, 0, 0, 0]

    # create a copy of the array. The [:] notation copies by value instead copying by reference
    #temp_array = array[:]
    split_array(array, temp_array, 0, len(array)-1)
    print array
