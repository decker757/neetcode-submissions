class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}
        result = []    

        for i in range(0, len(nums)):
            difference = 0
            difference = target - nums[i]

            n_dict[difference] = i

        for i in range(0, len(nums)):
            if nums[i] in n_dict:
                if i != n_dict[nums[i]]:
                    return [i,n_dict[nums[i]]]


            
        

        


            
