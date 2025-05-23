class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        return self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


s = Stack()


def main():
    print("Stack Implementation Simulation")
    while True:
        print()
        print("1. Add to stack")
        print("2. View Stack")
        print("3. Pop from Stack")
        print("4. Peek top element of stack")
        print("5. Check if stack is empty")
        print("6. Size of Stack")
        print("7. Exit")
        print()
        choice = input("Enter choice: ")
        match choice:
            case "1":
                element = input("Enter element: ")
                s.push(element)
            case "2":
                print("Stack:",s.stack)
            case "3":
                print("item popped:",s.pop())
            case "4":
                print("top element of stack:",s.peek())
            case "5":
                print("Is Stack empty:",s.is_empty())
            case "6":
                print("Size of stack:",s.size())
            case "7":
                print("You have exited the program!")
                break
            case _:
                print("Invalid option")


main()
