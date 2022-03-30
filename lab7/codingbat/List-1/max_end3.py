def max_end3(nums):
  m = max(nums[0], nums[2])
  nums[0], nums[1], nums[2] = m, m, m
  return nums