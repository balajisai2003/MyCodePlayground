# stones = [5,3,1,4,2]
# alice=0
# bob=0
# for i in range(len(stones)):
#     if i%2==0:
#         if stones[0]<=stones[-1]:
#             stones.pop(0)
#         else:
#             stones.pop(-1)
#         alice+=sum(stones)
#         print("alisce",alice)
#     else:
#         if i==len(stones)-2:
#             if stones[0] <= stones[-1]:
#                 stones.pop(0)
#             else:
#                 stones.pop(-1)
#             alice += sum(stones)
#             print("bob", alice)
#
#         elif stones[0]<=stones[-1]:
#             stones.pop(-1)
#         else:
#             stones.pop(0)
#         bob+=sum(stones)
#         print("bob",bob)
# print(alice-bob)

