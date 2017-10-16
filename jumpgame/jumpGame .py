nums = [1,1,1,2,0,0,2]

class Solution(object):
	def canJump(nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		index = 0
		jump = nums[index]
		
		while index < len(nums) and jump > 0:
		    jump = nums[index]
		    index = index+jump

		return index >= len(nums)-1

print(canJump(nums))
