# --- Directions
# Return the 'middle' node of a linked list.
# If the list has an even number of elements, return
# the node at the end of the first half of the list.
# *Do not* use a counter variable, *do not* retrieve
# the size of the list, and only iterate
# through the list one time.
# --- Example
#   const l = new LinkedList();
#   l.insertLast('a')
#   l.insertLast('b')
#   l.insertLast('c')
#   midpoint(l); // returns { data: 'b' }

class LinkedListNode(object):
  def __init__(self, value, nextNode):
    self.value = value
    self.nextNode = nextNode

class LinkedList(object):
  def __init__(self, head = None):
    self.head = head

  def add(self, NewNode):
    tmp = self.head
    # walk to the tail
    while(tmp.nextNode):
      tmp = tmp.nextNode
    tmp.nextNode = NewNode


n6 = LinkedListNode("meh6", None)
n5 = LinkedListNode("meh5", n6)
n4 = LinkedListNode("meh4", n5)
n3 = LinkedListNode("meh3", n4)
n2 = LinkedListNode("meh2", n3)
n1 = LinkedListNode("meh1", n2)

ll = LinkedList(n1)

n7 = LinkedListNode("meh7", None)
ll.add(n7)

# display linkedlist

tmp = ll.head
while(tmp):
  print(f'node: {tmp.value}, next node: {tmp.nextNode}')
  tmp = tmp.nextNode

def midpoint(linkedList):
  array_nodes = []
  # TODO: tbd

print(midpoint(ll))  
