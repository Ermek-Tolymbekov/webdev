def squirrel_play(temp, is_summer):
  if temp >= 60:
    return (is_summer and temp <= 100) or temp <= 90
  else:
    return False