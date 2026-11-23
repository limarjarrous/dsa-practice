# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        stack = []

        def get_number(stack):
            num = 0
            while stack:
                num *= 10
                num += stack.pop()
            return num
        
        def get_list(num):
            dummy = ListNode(0)
            current = dummy
            if num == 0:
                current.next = ListNode(0)
            else:
                while num:
                    current.next = ListNode(num % 10)
                    current = current.next
                    num //= 10
            return dummy.next
        
        while l1:
            stack.append(l1.val) 
            l1 = l1.next
        
        num1 = get_number(stack)
        

        while l2:
            stack.append(l2.val) 
            l2 = l2.next
        
        num2 = get_number(stack)
        

        return get_list(num1 + num2)