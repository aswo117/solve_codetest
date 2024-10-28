'''
최대 공약수(gcd)와 LinkedList 를 이용한 문제
1. leetcode에서 푸는 문제라 출력값을 어떻게 해야 될지 몰랐다. -> 그냥 return 하면 되는듯
2. 제공 api를 사용해도 되는 듯(gcd) linked list의 사용법은 c와 같은것 같고, head는 미리 선언되어 있는거 같음.
3. 앞으로도 ㅎㅇㅌ
'''

import sys

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        cur = head.next
        while cur:
            num = gcd(pre.val, cur.val)
            pre.next = ListNode(num, cur)
            pre = cur
            cur = cur.next
        return head
