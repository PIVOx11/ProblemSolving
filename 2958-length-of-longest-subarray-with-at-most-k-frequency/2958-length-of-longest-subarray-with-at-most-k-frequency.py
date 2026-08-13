class Solution:
    def maxSubarrayLength(self, n: List[int], k: int) -> int:
        ans = 0
        f = defaultdict(int)

        right = left = 0

        for right in range(len(n)):
            v = n[right]
            f[v] += 1

            if f[v] > k:
                ans = max(ans, right - left)
                while f[v] > k:
                    f[n[left]] -= 1
                    left += 1

        ans = max(ans, (right + 1) - left)

        return ans
