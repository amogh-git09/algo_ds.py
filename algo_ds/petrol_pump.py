class PetrolPump(object):
    def __init__(self, fuel, dist):
        self.fuel = fuel
        self.dist = dist

    def __str__(self):
        return "fuel: {}, dist: {}".format(self.fuel, self.dist)

def find_start(arr):
    n = len(arr)
    start = end = 0
    available = arr[start][0]
    required = arr[start][1]
    while (end + 1) % n != start:
        if available >= required:
            end = (end + 1) % n
            available += arr[end][0]
            required += arr[end][1]
        else:
            start -= 1
            if start == -1:
                start = n-1
            available += arr[start][0]
            required += arr[start][1]
    if available >= required:
        return start
    else:
        return -1

def find_start_linked_queue(queue):
    start = queue.head
    succ, start, stop_flag = try_journey(start, queue.head)
    while not (succ or stop_flag):
        succ, start, stop_flag = try_journey(start, queue.head)
    if succ:
        return start
    else:
        return None

def try_journey(start, head):
    if start.val.fuel < start.val.dist:
        return False, start.next, start.next is head
    stop_flag = False
    n = start
    c_fuel = n.val.fuel
    while c_fuel >= n.val.dist:
        c_fuel -= n.val.dist
        n = n.next
        if n is None:
            n = head
        if n is head:
            stop_flag = True
        if n is start:
            return True, start, stop_flag
        c_fuel += n.val.fuel
    return False, n, stop_flag
