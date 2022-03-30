def array123(nums):
  n = len(nums)
  seq = [1, 2, 3]
  if n > 3:
    for i in range(n - 2):
      if nums[i: i+3] == seq:
        return True
  else:
    return nums == seq
  return False
