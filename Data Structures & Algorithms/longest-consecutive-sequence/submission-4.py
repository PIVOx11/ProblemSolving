class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        map_seq = []
        value = None
        if not nums:
            return 0
        for i in nums:
            if i - 1 in nums:
                continue
            else:
                value = i
                counter += 1
                for x in range(len(nums)):
                    if value + 1 in nums:
                        value += 1
                        counter += 1
                    else:
                        map_seq.append(counter)
                        counter = 0
                        break
        
        return sorted(map_seq, reverse=True)[0] 