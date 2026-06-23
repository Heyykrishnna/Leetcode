class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        x = 10**9 + 7
        m = r - l + 1

        up = [i for i in range(m)]
        down = [m - 1 - i for i in range(m)]

        for n in range(n - 2):
            nu = [0] * m
            nd = [0] * m

            pref = 0
            for i in range(m):
                nu[i] = pref
                pref = (pref + down[i]) % x

            st = 0
            for i in range(m - 1, -1, -1):
                nd[i] = st
                st = (st + up[i]) % x

            up, down = nu, nd

        return (sum(up) + sum(down)) % x