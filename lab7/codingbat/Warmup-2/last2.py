def last2(str):
  last = str[-2:]
  cnt = 0
  for i in range(len(str)-2):
    if last == str[i:i+2]:
      cnt += 1
  return cnt