class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        r_C = Counter(r)
        m_C = Counter(m)

        for c in r_C:
            if c not in m_C or r_C[c] > m_C[c]:
                return False
        
        return True