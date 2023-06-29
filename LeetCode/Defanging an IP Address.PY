# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return "".join(
#             "[.]" if address[i] == "." else address[i]
#             for i in range( len(address))
#         )
# obj = Solution()
# print(obj.defangIPaddr("1.1.1.1"))

s="1.1.1.1"

print(s.replace(".","[.]"))