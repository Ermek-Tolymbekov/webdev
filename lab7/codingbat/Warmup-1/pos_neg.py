def pos_neg(a, b, negative):
  if negative == True:
    return a < 0 and b < 0
  else:
    return (a < 0) ^ (b < 0)