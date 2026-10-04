class Solution:
    def checkValidString(self, s: str) -> bool:
        oc = 0
        for c in s:
            if c == "(" or c == "*":
                oc += 1
            else:
                oc -= 1
            if oc < 0:
                return False

        cc = 0
        for c in reversed(s):
            if c == ")" or c == "*":
                cc += 1
            else:
                cc -= 1
            if cc < 0:
                return False

        return True