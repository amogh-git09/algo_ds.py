from linked_list import *

ll1 = LinkedList()
ll1.insert_at_end(Node(8))
ll1.insert_at_end(Node(2))
ll1.insert_at_end(Node(5))
ll1.insert_at_end(Node(4))
ll1.insert_at_end(Node(1))
ll1.insert_at_end(Node(22))
ll1.insert_at_end(Node(11))
ll1.insert_at_end(Node(6))
print(ll1)
ll1.reverse_groups(8)
print(ll1)
