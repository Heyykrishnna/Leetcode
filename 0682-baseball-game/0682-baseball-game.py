class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=0
        stack=[]
        for i in operations:
            if i =='+':
                a=stack[-2]+stack[-1]
                stack.append(a)
                ans+=a
            elif i=='C':
                ans-=stack.pop()
            elif i=='D':
                t=stack[-1]*2
                ans+=t
                stack.append(t)
            else:
                stack.append(int(i))
                ans+=int(i)
        return ans
        







        