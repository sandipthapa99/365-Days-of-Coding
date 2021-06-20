class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)

my_queue = Queue()

my_queue.enqueue('1')
my_queue.enqueue('2')
my_queue.enqueue('3')
my_queue.print_queue()

my_queue.dequeue()
my_queue.print_queue()

# =======
# Result:
# =====================================
# ['3','2','1']
# ['3','2']
# =====================================