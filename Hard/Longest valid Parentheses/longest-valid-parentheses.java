//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            String S = in.readLine();
            
            Solution ob = new Solution();
            System.out.println(ob.maxLength(S));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution{
    static int maxLength(String S){
        // code here
        
        Stack<Integer> st = new Stack<Integer>();
        for(int i = 0; i < S.length(); i++)
        {
            if(st.size() > 0 && (S.charAt(st.peek()) == '(' && S.charAt(i) == ')'))
            {
                st.pop();
            }
            else{
                st.push(i);
            }
        }
            int res = -1;
            int max = 0;
            
            for(int i : st)
            {
                max = Math.max(max, i-res-1);
                res = i;
            }   
            max = Math.max(max, S.length()-res-1);
            return max;
        }
    }