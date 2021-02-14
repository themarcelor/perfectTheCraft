import math

#n = 12345
n = -3456

def reverse_int(n):
  rev = ""
  sign = ""
  n = str(n)
  if '-' in n:
    sign = '-'
    n = n[1:]
    print(f'new n: {n}')

  for i in n:
    rev = i + rev

  return int(sign + rev)

# alternative
def reverseInt(n):
    pos_n = abs(n)
    rev = str(pos_n)[::-1]
    return int( int(rev) * math.copysign(1, float(n)) )

if __name__ == '__main__':
  print(reverse_int(n))
  print(reverseInt(n))
