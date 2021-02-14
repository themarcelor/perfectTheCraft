# Write a function that accepts a positive number N.
# The function should console log a step shape
# with N levels using the # character.  Make sure the
# step has spaces on the right hand side!
# --- Examples
#   steps(2)
#       '# '
#       '##'
#   steps(3)
#       '#  '
#       '## '
#       '###'
#   steps(4)
#       '#   '
#       '##  '
#       '### '
#       '####'

import timeit

# num of steps
num = 4

# best performance
def steps_mine(num):
    rows = []
    for i in range(0,num):
        h = i+1
        s = (num-i)-1

        #print(h,s)

        row = '#'*h
        row = row + '_'*s

        rows.append(row)
    return '\n'.join(rows)

def steps_rows_and_cols(num):
    stairs = []
    for r in range(0,num):
        stair = ''

        for c in range(0,num):
            if c <= r:
                stair = stair + '#'
            else:
                stair = stair + '_'
        stairs.append(stair)
    return '\n'.join(stairs)

def steps_recursion(num, row = 0, stairs = [], step = ''):
    if row == num:
        return '\n'.join(stairs)

    if len(step) == num:
        stairs.append(step)
        # increment row and reset step
        return steps_recursion(num, row + 1, stairs, '')

    add = '#' if len(step) <= row else '_'

    return steps_recursion(num, row, stairs, step + add)


def steps(n):
  output = ""
  line_length = n
  step = 1

  while step < n:
    for i in range(step):
      output += "#" * step
      output_gap = line_length - step
      # print(f'output gap: {output_gap}')
      if output_gap > 0:
        # print(f'missing spaces!, need to add {output_gap} spaces...')
        output += "_" * output_gap
      output += '\n'
      step += 1

  return output

if __name__ == '__main__':
    first = timeit.timeit("steps_mine(num)", "from __main__ import steps_mine, num", number=100)
    second = timeit.timeit("steps_rows_and_cols(num)", "from __main__ import steps_rows_and_cols, num", number=100)
    third = timeit.timeit("steps_recursion(num)", "from __main__ import steps_recursion, num", number=100)
    fourth = timeit.timeit("steps(num)", "from __main__ import steps, num", number=100)
    print(first, second, third, fourth)
