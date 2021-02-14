str = "whatever"

def reverse_string(str):
  new_string = ""
  for i in str:
    new_string = i + new_string
  return new_string

if __name__ == '__main__':
  print(reverse_string(str))
