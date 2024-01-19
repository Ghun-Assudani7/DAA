class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = QueueNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_item
        else:
            return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.front.data
        else:
            return "Queue is empty"

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count


# Example Usage:
queue_linked_list = QueueLinkedList()
queue_linked_list.enqueue(1)
queue_linked_list.enqueue(2)
queue_linked_list.enqueue(3)

print("Queue (Linked List) Front:", queue_linked_list.front())
print("Queue (Linked List) Dequeue:", queue_linked_list.dequeue())
print("Queue (Linked List) Size:", queue_linked_list.size())
