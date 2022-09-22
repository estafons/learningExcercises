from typing import List
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sumSoFar = sum([num for num in nums if num%2==0])
        for val, i in queries:

            if nums[i]%2 == 0:
                
                # integer was even till now.
                # substract the value from the total sum.
                # (otherwise the value would be added twice)
                sumSoFar -= nums[i]
            
            # add new value val to the value at index i. 
            nums[i] += val

            if nums[i]%2 == 0:
                # if new value is even, add to total sum.
                sumSoFar += nums[i]
            
            # append total sum of iteration to answer list.
            answer.append(sumSoFar)
        return answer

nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
x = Solution()
x.sumEvenAfterQueries(nums, queries)