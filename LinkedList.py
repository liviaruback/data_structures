class ListNode:
    
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedListNode:
    
    # create a new singly linked list - O(1) time
    def __init__(self):
        self.head = None
        
    # return a string representation of the list
    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.value))
            current = current.nextNode
        return '['+ ', '.join(nodes)+']'
            
    # insert a new element at the beginning - O(1) time
    def prepend(self, value):
        newNode = ListNode(value)
        newNode.nextNode = self.head
        self.head = newNode
        
    # insert a new element at the end - O(N) time
    def append(self, value):
        current = self.head
        while current.nextNode:
            current = current.nextNode
        newNode = ListNode(value)
        current.nextNode = newNode 
        
    # remove the first occurence of value in the list - O(N) time  
    def remove(self, data):
        current = self.head
        previous = None
        while current.nextNode and current.value != data:
            previous = current
            current = current.nextNode
    
        if previous is None:
            self.head = current.nextNode
        else:
            previous.nextNode = current.nextNode
            
    # reverse the Linked List in-place - O(N) time
    def reverse(self):
        current = self.head
        previous = None
        nextNode = None
        while current:
            nextNode = current.nextNode
            current.nextNode = previous
            previous = current
            current = nextNode
        self.head = previous
        
# creating a Singly Linked List

lst = LinkedListNode()

# inserting elements in the beginning
lst.prepend(2)
lst.prepend(1)

# inserting elements in the end
lst.append("three")
lst.append("last")
lst.append("items")

# reversing the list in place
lst.reverse()

lst