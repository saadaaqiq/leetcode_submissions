# https://leetcode.com/problems/encode-and-decode-tinyurl

class Codec:

    def __init__(self):
        self.long_to_short = {}
        self.short_to_long = {}
        self.last = 0

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.long_to_short:
            self.long_to_short[longUrl] = self.last
            self.short_to_long[self.last] = longUrl
            self.last += 1
        return self.long_to_short[longUrl]
            
    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.short_to_long:
            return self.short_to_long[shortUrl]