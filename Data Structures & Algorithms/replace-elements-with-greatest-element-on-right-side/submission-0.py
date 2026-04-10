class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # navigating arr from the end / reverse
        # init max = -1
        # new max = max(oldmax, arr[i])
        right_max = -1
        for num in range(len(arr) -1, -1, -1):
            # compute the new max before overwriting first value
            new_max = max(right_max, arr[num])
            #replace current value with set max
            arr[num] = right_max
            #update right max with new max just found
            right_max = new_max
        return arr