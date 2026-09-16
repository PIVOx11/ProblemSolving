class Solution:
    def candy(self, r: list[int]) -> int:
        l = len(r)
        ans = [1] * l
        i = 0
        while i < l:
            if i > 0 and r[i] > r[i - 1]:
                ans[i] = ans[i - 1] + 1
            i += 1

        i = l - 1
        while i >= 0:
            if i + 1 < l and r[i] > r[i + 1]:
                if ans[i] <= ans[i + 1]:
                    ans[i] = ans[i + 1] + 1
            i -= 1
        return sum(ans)