class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_list = Counter(nums)
        map_list = sorted(map_list, key=lambda x: map_list[x], reverse=True)
        result = []
        for i in range(k):
            result.append(map_list[i])
        return result
