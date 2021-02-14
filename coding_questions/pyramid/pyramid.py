# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a pyramid shape
# with N levels using the # character.  Make sure the
# pyramid has spaces on both the left *and* right hand sides
# --- Examples
#   pyramid(1)
#       '#'
#   pyramid(2)
#       ' # '
#       '###'
#   pyramid(3)
#       '  #  '
#       ' ### '
#       '#####'
        #######
       #########
      ###########
     #############

n = 7

def pyramid(n):
  output = ""

  for i in range(0, n):
    spaces = "_" * ( (n - i) -1 ) if i <= n else ""
    center = "#" * ( 1 + (i * 2) )
    output += spaces + center + spaces + "\n"

  return output

if __name__ == '__main__':
  print(pyramid(n))
