# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans  = ListNode()
        while list1.next and list2.next:
            if list1.val < list2.val:
                ans.next = list1
                list1 ,ans = list1.next,list1
            else :
                ans.next = list2
                list2 ,ans = list2.next,list2
        if list1.next or list2.next:
            ans.next = list1 if list1 else list2
        
        return ans.next
    