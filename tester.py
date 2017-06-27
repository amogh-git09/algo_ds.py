from linked_list import *

ll1 = LinkedList()
ll1.insert_at_end(Node(9))
ll1.insert_at_end(Node(9))
ll1.insert_at_end(Node(9))
ll2 = LinkedList()
ll2.insert_at_end(Node(1))
print(ll1)
print(ll2)
ll3 = LinkedList.add(ll1, ll2)
print(ll3)
