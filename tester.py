from linked_list import *
from node import *

ll1 = LinkedList()
ll1.insert_at_end(Node(1))
ll1.insert_at_end(Node(2))
ll1.insert_at_end(Node(3))
ll1.insert_at_end(Node(4))
print(ll1)
ll1.rotate(2)
print(ll1)
