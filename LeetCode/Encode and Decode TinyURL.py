import random

class Codec:
    def __init__(self):
        self.shrotUrlDict = {}
        self.letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.digits = list('0123456789')

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            shortUrl = f'http://tinyurl.com/{self.ranGen()}'
            if shortUrl not in self.shrotUrlDict:
                self.shrotUrlDict[shortUrl] = longUrl
                return shortUrl
        

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shrotUrlDict[shortUrl]
        
    def ranGen(self):
        return "".join(random.choice(self.letters+self.digits) for _ in range(6))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))