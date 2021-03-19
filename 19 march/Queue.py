def enqueue( front, rear, size):
    queue = []
    if(rear + 1) % size == front:
        print("Queue is Full")
    else:
        rear = (rear + 1) % size
        queue.append(eval(input("Enter an element: ")))
        front += 1
        return front, rear, queue

# def dequeue(front, rear, size):
#     if front == -1:
#         print("queue is empty")
#     else

size = eval(input("Enter Size of the Queue: "))
queue = []
front = rear = -1

front, rear, queue = enqueue(front, rear, size)
print(queue)