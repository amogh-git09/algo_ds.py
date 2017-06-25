from linked_list import *

ll = LinkedList()
ll.insert_at_end(Node(8))
ll.insert_at_end(Node(2))
ll.insert_at_end(Node(5))
ll.insert_at_end(Node(4))
ll.insert_at_end(Node(1))
ll.insert_at_end(Node(22))
node1 = Node(11)
ll.insert_at_end(node1)
node2 = Node(6)
ll.insert_at_end(node2)
node2.next = node1
ll.remove_cycle()
print(ll)
