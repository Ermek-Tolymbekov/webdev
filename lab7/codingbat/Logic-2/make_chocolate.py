def make_chocolate(small, big, goal):
  if goal // 5 <= big:
    if small - goal%5 >= 0:
      return goal%5
    else:
      return -1
  else:
    goal -= big*5
    if goal > small:
      return -1
    else:
      return goal