class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        numDict = defaultdict(int)

        for n in nums:
            numDict[n] += 1

        for i in range(len(nums)):
            numDict[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums)):
                numDict[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                
                target = -(nums[i] + nums[j])
                if numDict[target] > 0:
                    res.append([nums[i], nums[j], target])
            
            for j in range(i + 1, len(nums)):
                numDict[nums[j]] += 1
        
        return res

