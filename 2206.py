# 1.) Passed testcases!
# 2.) Solution accepted!
class Solution:
  def divideArray(self, nums: List[int]) -> bool:
        arr_01 = []
        arr_02 = []
        nums.sort()
        for i, val in enumerate(nums):
            if i % 2 == 0:
                arr_01.append(val)
            else:
                arr_02.append(val)

        return arr_01 == arr_02


# 1.) Passed testcases!
# 2.) Solution accepted! (more efficient solution)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i + 1]:
                return False

        return True
