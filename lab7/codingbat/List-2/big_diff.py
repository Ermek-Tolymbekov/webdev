def big_diff(nums):
  mi = nums[0]
  ma = 0
  for i in nums:
    mi = min(mi, i)
    ma = max(ma, i)
  return ma - mi