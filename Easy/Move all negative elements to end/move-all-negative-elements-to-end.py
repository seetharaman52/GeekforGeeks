#User function Template for python3
import numpy as np
class Solution:
    def segregateElements(self, arr, n):

        lst=[]
        lst1=[]
        for i in arr:
            if i>=0:
                lst.append(i)
            else:
                lst1.append(i)

        val=lst+lst1

        arr[:]=val

        return val
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends