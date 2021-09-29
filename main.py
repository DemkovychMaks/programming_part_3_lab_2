class Node :

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None

    def insert_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_rear(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        rear = self.head
        while rear.next:
            rear = rear.next
        rear.next = new_node
        new_node.prev = rear
        return

    def get_front(self):
        print("Front element is:", self.head.data)
        print()
        return self.head.data

    def get_last(self):
        rear = self.head
        while rear.next:
            rear = rear.next
        print("Last element is:", rear.data)
        print()
        return rear.data

    def delete_front(self):
        self.head = self.head.next

    def delete_last(self):
        rear = self.head
        while rear.next:
            rear = rear.next
        rear.prev.next = None

    def exist(self, data):
        rear = self.head
        while rear.next:
            if rear.data == data:
                print(f"Element {data} is present in the deque")
                return
            rear = rear.next
        print(f"Element {data} is not present in the deque")
        return

    def deque_to_list(self):
        output = list()
        node = self.head
        while node is not None:
            output.append(node.data)
            node = node.next
        return output

    @staticmethod
    def print_deque(node):
        print("\nDeque")
        while node:
            print(node.data, end=" ")
            node = node.next
        print()

if __name__ == '__main__':
    deque = Deque()
    deque.insert_front(20)
    deque.insert_front(40)
    deque.insert_front(10)

    deque.insert_rear(80)
    deque.insert_rear(60)

    deque.print_deque(deque.head)

    deque.delete_front()
    deque.delete_last()

    deque.print_deque(deque.head)

    deque.get_front()
    deque.get_last()

    deque.exist(60)
    deque.exist(100)