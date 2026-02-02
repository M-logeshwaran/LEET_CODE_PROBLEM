/* Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6 */

//CODE

class Solution {
public:
    int lengthOfLastWord(string s) {
            s.erase(0,s.find_first_not_of(" \t\n\r"));
            s.erase(s.find_last_not_of(" \t\n\r")+1);
        int b = s.rfind(' ');
        int len = (s.length()-1)-b;
        return len;
    }
};

