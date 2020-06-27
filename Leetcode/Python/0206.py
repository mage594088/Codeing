class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
#head.next.next.next.next.next = ListNode(6)

r = None
q = None
p = head
count = 0

while p:
    r = q
    q = p
    p = p.next
    q.next = r
    count += 1

print('count:', count)
head = q

while head:
    print(head.val)
    head = head.next