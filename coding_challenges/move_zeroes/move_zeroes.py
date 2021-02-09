array = [0,1,0,3,12]
#array = [0,0,1]

def swap(a, b, array):
  tmp = array[a]
  array[a] = array[b]
  array[b] = tmp

def move_zeroes(array):
  for idx, i in enumerate(array):
    print(f'iteration: {i}')
    if i != 0:
      print(f'found non zero: {i} at index: {idx}')
      # look at previous elements and swap indices if there are any zeroes
      for p in range(idx):
        # keep walking from the begining of the array to look for the left-most zero
        if array[p] == 0:
          swap(idx, p, array)
          print(f'after swap: {array}')

  return array

print(move_zeroes(array))
