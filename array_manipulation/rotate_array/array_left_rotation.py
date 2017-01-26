# -*- coding: utf-8 -*-
"""
A left rotation operation on an array of size  shifts each of the array's elements  unit to the left.
 For example, if left rotations are performed on array , then the array would become.

"""


def array_left_rotation(a, n, k):
    answer = []
    for i in range(n):
        if(len(a) > i+k):
            answer.append(a[k+i])
        else:
            answer.append(a[k+i - len(a)])
    return answer
    


if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation(a, n, k)
    print(*answer, sep=' ')