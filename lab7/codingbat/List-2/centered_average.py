def centered_average(nums):
  mi = nums[0]
  ma = 0
  sum = 0
  for i in nums:
    mi = min(mi, i)
    ma = max(ma, i)
    sum += i
  return (sum-mi-ma) // (len(nums)-2)