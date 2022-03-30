def sum13(nums):
  if len(nums) == 0:
    return 0
  else:
    sum = 0
    b = bool(False)
    for i in nums:
      if i == 13:
        b = True
      elif b:
        b = False
      else:
        sum += i
    return sum