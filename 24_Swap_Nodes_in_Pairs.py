# Problem No- 24. Swap Nodes in Pairs
'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

'''

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        d1 = d =ListNode(0)
        d.next = head
        
        while d.next and  d.next.next:
            p = d.next
            q = d.next.next
            d.next,p.next,q.next = q,q.next,p
            d = p
        return d1.next
