'''Write a function to reverse a linked list'''
#Doubt
def reverse(head):
    current = head
    previous = None
    nextNode = None

    while current:
        # print(current.value)
        nextNode = current.nextNode
        current.nextNode = previous
        previous = current
        current = nextNode

    return previous

class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c
# c.nextNode = a

reverse(a)

print(c.value)
print(c.nextNode.value)
print(b.nextNode.value)


