class Codec:
    urlDict = {}
    stem = 'https://tinyurl.com/'
    code = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        shortUrl = self.stem + str(self.code)
        self.urlDict[shortUrl] = longUrl
        self.code += 1
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return (self.urlDict[shortUrl])

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))