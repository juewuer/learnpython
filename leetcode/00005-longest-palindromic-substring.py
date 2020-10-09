
class Solution:
    def longestPalindrome(self, s: str) -> str:
        i=0
        length=len(s)
        maxlen = 0
        maxstr = ''
        while(i<length):
            start =i
            end =i+1
            while end<length and s[end] == s[i]:
                end+=1
            i = end
            while True:
                start -= 1
                if start<0 or end>=length or s[start] != s[end]:
                    break
                end += 1

            if maxlen < end -start -1:
                maxlen = end -start -1
                maxstr = s[start+1:end]

        return maxstr

import pytest
if __name__=="__main__":
    s = Solution()
    #print(s.longestPalindrome(''))
    #print(s.longestPalindrome('b'))
    #print(s.longestPalindrome('babad'))
    #print(s.longestPalindrome('cbbd'))
    print(s.longestPalindrome('bananas'))
    assert s.longestPalindrome("bananas") in ["anana"]
    assert s.longestPalindrome('babad') in ['bab','aba']

    assert s.longestPalindrome('cbbd') in ['bb']