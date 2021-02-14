str = "Socorram me subi no onibus em Marrocos"

def is_palindrome(str):
  rev = ""
  str = str.lower().replace(' ', '')
  for i in str:
    rev = i + rev

  print(f'string: {str}')
  print(f'reverse: {rev}')
  if str == rev:
    return True
  return False

if __name__ == '__main__':
  print(is_palindrome(str))
