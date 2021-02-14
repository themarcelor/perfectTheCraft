str = 'hello world'

def max_chars(str):
  chars = {}

  for c in str:
    chars.__setitem__(c, chars[c] + 1) if c in chars else chars.__setitem__(c, 1)

  print(f'chars: {chars}')

  max = (0, 0)
  for k,v in chars.items():
    if v > max[1]:
      max = (k, v)

  return max[0]

if __name__ == '__main__':
  print(max_chars(str))
