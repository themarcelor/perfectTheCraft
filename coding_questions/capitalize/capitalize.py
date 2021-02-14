sentence = "a short sentence"

def capitalize(sentence):
  new_sentence = ""
  for i in range(0, len(sentence)):
      new_sentence += sentence[i].upper() if i == 0 or  sentence[i-1] == " " else sentence[i]

  return new_sentence


if __name__ == '__main__':
  print(capitalize(sentence))
