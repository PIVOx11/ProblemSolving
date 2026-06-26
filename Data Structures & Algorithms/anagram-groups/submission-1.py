class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        result = []
        for word in strs:
            new_str = sorted(word)
            new_str = "".join(new_str)
            if new_str not in word_map:
                word_map[new_str] = []
            word_map[new_str].append(word)
        for lst in word_map.values():
            result.append(lst)
        return sorted(result, key=len)