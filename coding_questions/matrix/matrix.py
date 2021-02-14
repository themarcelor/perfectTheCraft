# --- Directions
# Write a function that accepts an integer N
# and returns a NxN spiral matrix.
# --- Examples
#   matrix(2)
#     [[1, 2],
#     [4, 3]]
#   matrix(3)
#     [[1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]]
#  matrix(4)
#     [[1,   2,  3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10,  9,  8, 7]]

def matrix(n):
  inner_array = []
  outer_array = []
  counter = 0
  for i in range(n):
    for j in range(n):
      if i > 0 and j == 0:
        # resume counter from the last element of the previous inner array
        counter = outer_array[i-1][n-1]
      counter = counter + 1
      inner_array.append(counter)
      print(f'counter: {counter}')
    
    outer_array.append(inner_array)
    inner_array = []

  return outer_array

if __name__ == '__main__':
  print(matrix(4))
