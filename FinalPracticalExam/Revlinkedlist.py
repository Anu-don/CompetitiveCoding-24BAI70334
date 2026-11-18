class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def Rev_lnkedList(head):
    rev = None
    curr = head
    while curr:
        new = Node(curr.value)
        new.next = rev
        rev = new
        curr = curr.next

    c1 = head
    c2 = rev
    while c1 and c2:
        if c1.value != c2.value:
            return False
        c1 = c1.next
        c2 = c2.next

    return True


def display(head):
    ans = Rev_lnkedList(head)
    if ans:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")


if __name__ == "__main__":
    print(" " * 10, "> Reversed LinkedList <")
    print()

    n = int(input("Enter Length of linked list :"))
    print()

    if n <= 0:
        head = None
    else:
        head = Node(int(input("Enter Element :")))
        new = head
        for i in range(n - 1):
            new2 = Node(int(input("Enter Element :")))
            new.next = new2
            new = new.next

    print()
    display(head)
