# Node class
class Node:
    """
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    """
    def __init__(self, name):
        self.name = name
        self.next = None


# LinkedList class
class LinkedList:
    """
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    """
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} added to the front of the waitlist.")

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:  # List is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"{name} added to the end of the waitlist.")

    def remove(self, name):
        current = self.head
        prev = None

        while current:
            if current.name == name:
                if prev:  # Node is not head
                    prev.next = current.next
                else:  # Node is head
                    self.head = current.next
                print(f"Removed {name} from the waitlist.")
                return
            prev = current
            current = current.next

        print(f"{name} not found.")

    def print_list(self):
        if not self.head:
            print("The waitlist is empty.")
            return

        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next


# Command-line interface
def waitlist_generator():
    waitlist = LinkedList()  # Create a new linked list instance

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)

        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Start the program
if __name__ == "__main__":
    waitlist_generator()


'''
Design Memo:
- How does your list work?
    The waitlist is implemented as a singly linked list, where each Node stores a customer's name
    and a reference to the next Node. The head represents the first customer, and each subsequent
    Node points to the next customer in line. Things like adding or removing someone
    involve updating the head and/or next pointers to make sure we keep the order.

- What role does the head play?
    The head is the entry point to the linked list. It represents the first customer in the waitlist.
    When adding to the front, the head is updated to point to the new Node. When removing the head,
    the head is updated to the next Node. All traversal starts from the head.

- When might a real engineer need a custom list like this?
    Custom linked lists are useful when you need dynamic data structures that allow efficient
    insertions and deletions at arbitrary positions without shifting elements like in arrays.
    For example, managing a real-time waitlist, task scheduling, or handling streaming data.
'''
