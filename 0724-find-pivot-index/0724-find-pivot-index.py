class Solution:
    def pivotIndex(self, n: List[int]) -> int:
        s = sum(n)
        l = len(n)
        arr = [0] * (l + 1)

        for i in range(l + 1):
            if i > 0:
                arr[i] = arr[i - 1] + n[i - 1]

        print(arr)

        for i in range(l):
            if ((s - n[i]) / 2) == arr[i]:
                return i

        return -1
