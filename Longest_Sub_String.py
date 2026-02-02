''' Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. '''

#CODE

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=[]
        a=''
        for i in s:
            if(i not in a):
                a=a+i
            else:
                k=a.index(i)
                l.append(a)
                a=a[k+1:]+i          
        b=0
        l.append(a)      
        for i in l:
            if(b<len(i)):
                b=len(i)
        return b        


        
