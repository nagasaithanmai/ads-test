class KStacks:
    def __init__(self, num_stacks, capacity):
        self.num_stacks = num_stacks
        self.capacity = capacity
        self.arr = [0] * capacity  # The main array to store elements
        self.top = [-1] * num_stacks  # Stores the top index for each stack
        self.next = [i + 1 for i in range(capacity - 1)] + [-1]  # Stores the next free slot
        self.free = 0  # Points to the first free slot

    def is_empty(self, stack_num):
        return self.top[stack_num] == -1

    def is_full(self):
        return self.free == -1

    def push(self, item, stack_num):
        if self.is_full():
            print("Stack Overflow!")
            return

        # Get the next free slot
        insert_index = self.free
        self.free = self.next[insert_index]

        # Place the item in the array
        self.arr[insert_index] = item

        # Update the 'next' pointer for the new item to point to the previous top of its stack
        self.next[insert_index] = self.top[stack_num]

        # Update the top of the stack
        self.top[stack_num] = insert_index

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            print("Stack Underflow!")
            return None

        # Get the index of the top element
        pop_index = self.top[stack_num]

        # Update the top of the stack to the previous element
        self.top[stack_num] = self.next[pop_index]

        # Add the popped slot back to the free list
        self.next[pop_index] = self.free
        self.free = pop_index

        return self.arr[pop_index]

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return None
        return self.arr[self.top[stack_num]]

# Example Usage:
if __name__ == "__main__":
    kstacks = KStacks(num_stacks=3, capacity=10)

    kstacks.push(10, 0)
    kstacks.push(20, 0)
    kstacks.push(30, 1)
    kstacks.push(40, 2)
    kstacks.push(50, 1)

    print(f"Pop from stack 0: {kstacks.pop(0)}")
    print(f"Peek at stack 1: {kstacks.peek(1)}")
    print(f"Pop from stack 1: {kstacks.pop(1)}")
    print(f"Pop from stack 2: {kstacks.pop(2)}")
    print(f"Pop from stack 1: {kstacks.pop(1)}")
    print(f"Pop from stack 0: {kstacks.pop(0)}")
    print(f"Pop from stack 0: {kstacks.pop(0)}") # Should show Stack Underflow
