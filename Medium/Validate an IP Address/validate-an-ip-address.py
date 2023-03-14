#User function Template for python3

def isValid(s):
    
    validSet = set([str(i) for i in range(256)])

    ipArray = s.split(".")

    if len(ipArray) != 4:

        return False

    for item in ipArray:

        if item not in validSet:

            return False

    return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends