class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Create a dummy node for the result
    dummy = ListNode()
    current = dummy  # Current node for the result linked list
    carry = 0  # Carry-over variable

    # Iterate through the linked lists
    while l1 or l2 or carry:
        x = l1.val if l1 else 0  # Value of current node in l1 or 0
        y = l2.val if l2 else 0  # Value of current node in l2 or 0

        # Compute the sum of digits and carry-over
        sum = x + y + carry
        carry = sum // 10  # Compute the carry-over
        current.next = ListNode(sum % 10)  # Create a new node with the digit sum

        # Move to the next nodes
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    result = []
    current = dummy.next
    while current:
        result.append(current.val)
        current = current.next

    return result


def createLinkedList(values):
    head = None
    prev = None
    for val in values:
        node = ListNode(val)
        if not head:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


# Take input for the first linked list
values1 = list(map(int, input("Enter values for the first linked list (space-separated): ").split()))
l1 = createLinkedList(values1)

# Take input for the second linked list
values2 = list(map(int, input("Enter values for the second linked list (space-separated): ").split()))
l2 = createLinkedList(values2)

# Add the two numbers and get the result as an array
result = addTwoNumbers(l1, l2)

# Print the result
print("Sum of the two linked lists:")
print(result)
