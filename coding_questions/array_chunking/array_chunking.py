#array = [1, 2, 3, 4] # split into 2 chunks
array = [1, 2, 3, 4, 5]

def array_chunking(array, chunks):
  new_array = []
  prev_pointer = 0
  for i in range(0, len(array), chunks):
    chunk_limit = i+chunks
    new_array.append(array[prev_pointer:chunk_limit])
    prev_pointer = chunk_limit

  return new_array

if __name__ == '__main__':
  print(array_chunking(array, 3))
