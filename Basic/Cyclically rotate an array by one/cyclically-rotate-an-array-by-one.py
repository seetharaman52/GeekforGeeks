#User function Template for python3

def rotate(arr, n):
    lis = arr[-1:]
    lis1 = arr[0:len(arr)-1]
    a = lis + lis1
    arr[:] = a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends