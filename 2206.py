class Solution:
    
  # 1.) Passed testcases!
  # 2.) Solution accepted!
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
