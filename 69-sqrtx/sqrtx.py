class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            print(0)
            return x

        root=0
        l,r=0,x

        while l<=r:
            m = (l+r)//2
            if m**2==x:
                return m
            elif m**2<x:
                l=m+1
                root=m
            else:
                r=m-1
        return root