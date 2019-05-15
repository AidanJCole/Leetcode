class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_string = ''
        builtstring = ''
        for l in s:
            if l not in builtstring:
                builtstring += l
            else:
                builtstring = builtstring[builtstring.index(l)+1:]+l
            if len(longest_string) < len(builtstring):
                longest_string = builtstring
        return len(longest_string)