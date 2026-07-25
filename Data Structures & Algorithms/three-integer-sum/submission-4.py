class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        for i in range(len(nums)):
            count[nums[i]] -= 1

            if i and nums[i - 1] == nums [i]:
                continue
            
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])
            
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return res