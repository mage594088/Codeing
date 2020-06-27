class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

curr = head = ListNode(0)
            
while l1 and l2:
    if l1.val < l2.val:
        curr.next = l1
        l1 = l1.next
    else:
        curr.next = l2
        l2 = l2.next
    curr = curr.next
curr.next = l1 or l2

while head.next:
    print(head.next.val)
    head = head.next

        