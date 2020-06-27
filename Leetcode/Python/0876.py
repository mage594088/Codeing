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

tmp = head
count = 0
while tmp:
    if tmp:
        count += 1
    tmp = tmp.next

tmp = head
for i in range(count//2):
    tmp = tmp.next

print(tmp.val)
