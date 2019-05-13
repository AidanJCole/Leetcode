class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        split = []
        for adr in emails:
            split.append(adr.split('@'))
        for addr in split:
            addr[0] = addr[0].split('+')[0].replace('.','')
        split = map(lambda x: tuple(x), split)
        return len(set(split))