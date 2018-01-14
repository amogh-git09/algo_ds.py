import sys

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L

def insert_after(node, new_node):
    """
    Inserts new_node after node.
    """
    new_node.next = node.next
    node.next = new_node

def insert_end(L, node):
    """
    Appends node at the end of L.
    L and node are both ListNodes.
    """
    n = L
    while n.next:
        n = n.next
    n.next = node

def delete_after(node):
    """
    Deletes node.next from the list.
    Assumes that node is not the tail node.
    """
    node.next = node.next.next

def merge(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next 
