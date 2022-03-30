def sum67(nums):
  if len(nums) == 0:
    return 0
  else:
    sum = 0
    b = bool(False)
    for i in nums:
      if i == 7 and b:
        b = False
      elif i == 6:
        b = True
      elif not b:
        sum += i
    return sum