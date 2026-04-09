class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # int array = nums
        # int val
        # remove all occurences of val from nums IN-PLACE, NO NEW ARRAY

        k = 0 # next time we find a non val value, where should we put it? 
        for i in range(len(nums)):
            if nums[i] != val: # don't want to take the special value and put at beginning, only val needs to move
                # similar to parition quicksort
                nums[k] = nums[i]
                k +=1
        return k
