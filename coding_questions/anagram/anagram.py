str1 = 'rail safety'
str2 = 'fairy tales'

def is_anagram(str1, str2):
  chars1 = {}
  chars2 = {}
  if len(str1) == len(str2):
    for s1, s2 in zip(str1, str2):
        chars1.__setitem__(s1, chars1[s1] + 1) if s1 in chars1 else chars1.__setitem__(s1, 1)
        chars2.__setitem__(s2, chars2[s1] + 1) if s2 in chars2 else chars2.__setitem__(s2, 1)

    if chars1 == chars2:
      return True
  else:
    return False

if __name__ == '__main__':
  print(is_anagram(str1, str2))
