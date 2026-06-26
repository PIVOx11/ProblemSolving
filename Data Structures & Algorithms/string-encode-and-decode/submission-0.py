class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        i = 0
        while i < len(strs):
            if not strs[i]:
                result = result + str(ord("\0"))
                result = result + " + "
                i += 1
                continue
            for c in strs[i]:
                result = result + str(ord(c)) + " "
            if i < len(strs) - 1:
                result = result + " + "
            i += 1
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        collab = ""
        s = s.split(" + ")
        if "" in s:
            s.remove("")
        for st in s:
            st = st.split()
            if st[0] == "0":
                result.append("")
                continue
            for c in st:
                collab = collab + chr(int(c))

            result.append(collab)
            collab = ""
        return(result)