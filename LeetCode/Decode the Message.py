class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s = "abcdefghijklmnopqrstuvwxyz"
        key = key.replace(" ","")
        c = 0
        d = {" ": " "}
        for i in range(len(key)):
            if key[i] not in d:
                d[key[i]] = s[c]
                c+=1
        return "".join(d[i] for i in message)
obj = Solution()
print(obj.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))