# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        def get_mid(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(head1, head2):
            merged_list = ListNode(-1)
            dummy = merged_list

            while head1 and head2:
                if head1.val <= head2.val:
                    dummy.next = head1
                    head1 = head1.next
                else:
                    dummy.next = head2
                    head2 = head2.next
                dummy = dummy.next
            
            if head1:
                dummy.next = head1
            if head2:
                dummy.next = head2
            
            return merged_list.next
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            mid = get_mid(head)
            right_head = mid.next
            mid.next = None

            left = merge_sort(head)
            right = merge_sort(right_head)
            return merge(left, right)
        
        return merge_sort(head)