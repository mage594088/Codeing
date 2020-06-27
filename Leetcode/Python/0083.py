class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)


curr = output = ListNode(0)
dict = {}
while head:
    if head.val not in dict:
        dict[head.val] = 1
        print(head.val)
        tmp = ListNode(head.val)
        curr.next = tmp
        head = head.next
        curr = curr.next
    else:
        head = head.next
    
    
print()
while output.next:
    print(output.next.val)
    output = output.next

        