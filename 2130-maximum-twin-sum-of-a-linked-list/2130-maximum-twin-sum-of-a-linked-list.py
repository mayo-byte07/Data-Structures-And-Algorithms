class Solution(object):
    def pairSum(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first_half = head
        second_half = prev 
        max_sum = 0
        
        while second_half:
            current_sum = first_half.val + second_half.val
            if current_sum > max_sum:
                max_sum = current_sum
                
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum