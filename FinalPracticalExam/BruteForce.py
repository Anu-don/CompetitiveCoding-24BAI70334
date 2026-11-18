class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def Palinelist(head):
    lis = []
    curr = head
    while curr:
        lis.append(curr.value)
        curr = curr.next

    n = len(lis)
    for i in range(n // 2):
        if lis[i] != lis[n - 1 - i]:
            return False

    return True


def display(head):
    ans = Palinelist(head)
    if ans:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")


if __name__ == "__main__":
    print(" " * 10, "> Brute Force <")
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
