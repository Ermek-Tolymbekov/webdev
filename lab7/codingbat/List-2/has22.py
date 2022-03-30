def has22(nums):
  two = [2, 2]
  for i in range(len(nums) - 1):
    if nums[i:i+2] == two:
      return True
  return False