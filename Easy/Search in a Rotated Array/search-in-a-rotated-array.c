//{ Driver Code Starts
//Initial Template for C

#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        int A[n];
        for(int i = 0; i < n; i++)
            scanf("%d",&A[i]);
        int key;
        scanf("%d",&key);
        int answer = search(A, 0, n - 1, key); 
        printf("%d\n",answer);
    }
return 0;
}

// } Driver Code Ends


//User function Template for C


    
int search(int A[], int l, int h, int key) { 
    int n = h-l+1;
       int low = 0, high = n-1;

       int rot = -1;
       while(low <= high){
           int mid = low + (high - low) / 2;
           if(A[mid] <= A[h]){
               rot = mid;
               high = mid - 1;
           }else{
               low = mid + 1;
           }
       }

       while(l <= h){
            int mid = l + (h-l) / 2;
            int realMid = (mid + rot) % n;
            if(A[realMid] == key)
                return realMid;
            if(A[realMid] < key) 
                l = mid + 1;
            else
                h = mid - 1;
       }
       
       return -1;
    }
    
