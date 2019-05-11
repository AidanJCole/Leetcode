class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ut = set()
        mapper = {}
        for l in 'abcdefghijklmnopqrstuvwxyz':
            mapper[l] = code.pop(0)
        for w in words:
            ut.add(''.join(map(lambda x: mapper[x], w)))
        return len(ut)