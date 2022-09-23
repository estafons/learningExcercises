from typing import List


class Solution1:
    """Single answer is expected in leetcode. Also, 
    indexes are requested instead of numbers.
    for a more versatile solution see below"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        helpDict = {}
        for k, v in enumerate(nums):
            if v in helpDict:
                helpDict[v].append(k)
            else:
                helpDict[v] = [k]
        answer = []
        for idx, num in enumerate(nums):
            if (target - num) in helpDict:
                if helpDict[target - num] != [idx]:
                    answer.extend([idx, helpDict[target - num][0]])
        answer = set(answer)
        return answer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        helpDict = {}
        for k, v in enumerate(nums):
            if v in helpDict:
                helpDict[v].append(k)
            else:
                helpDict[v] = [k]
        answer = []
        for idx, num in enumerate(nums):
            if (target - num) in helpDict:
                if helpDict[target - num] != [idx] \
                    and [num, target - num] not in answer \
                        and [target - num, num] not in answer:
                    answer.append([num, target - num])
        return answer



num = [2,7,11,15,0,2,7,11,15]
target = 9
x = Solution()

print(x.twoSum(num, target))