class Node():
  def __init__(self,value):
    self.data = value
    self.next = None
    self.prev = None

  def __str__(self): 
    return str(self.__dict__)

class LinkedList():
  def __init__(self,value):
    newNode = Node(value)
    self.head = newNode
    self.tail = self.head
    self.length = 1

  def __str__(self): 
    return str(self.__dict__)

  def prepend(self,value):
    prevHeadNode = self.head
    newNode = Node(value)
    self.head = newNode
    newNode.next = prevHeadNode
    prevHeadNode.prev = newNode
    self.length += 1

  def append(self,value):
    prevTailNode = self.tail
    newNode = Node(value) 
    prevTailNode.next = newNode
    newNode.prev = prevTailNode
    self.tail = newNode
    self.length += 1

  def printList(self):
    listArr = []
    currentNode = self.head
    while currentNode is not None:
      listArr.append(currentNode.data)
      currentNode = currentNode.next
    print("Linked List: ", listArr, "& Length: ", self.length)

  def printListReverse(self):
    listArr = []
    currentNode = self.tail
    while currentNode is not None:
      listArr.append(currentNode.data)
      currentNode = currentNode.prev
    print("Reversed Linked List: ", listArr, "& Length: ", self.length)

  def insert(self,index,value):
    if index == 0 :
      self.prepend(value)
    if index >= self.length :
      self.append(value)
    elif index > 0 and index < self.length :
      newNode = Node(value)
      
      if(index <= self.length/2):
        currentNode = self.head
        counter = 0
        while counter < index:
          currentNode = currentNode.next
          counter += 1
        currentNode.prev.next = newNode
        newNode.prev = currentNode.prev
        newNode.next = currentNode
        currentNode.prev = newNode
        self.length += 1
      else:
        currentNode = self.tail
        counter = self.length-1
        while counter > index:
          currentNode = currentNode.prev
          counter -= 1
        currentNode.prev.next = newNode
        newNode.prev = currentNode.prev
        newNode.next = currentNode
        currentNode.prev = newNode
        self.length += 1


  def remove(self,index):
    if index == 0:
      self.head = self.head.next
      self.head.prev = None
      self.length -= 1

    elif index == self.length-1:
      currentNode = self.tail
      self.tail = currentNode.prev
      currentNode.prev.next = None
      self.length -= 1

    elif index > 0 and index < self.length-1:
      if(index <= self.length/2):
        currentNode = self.head
        counter = 0
        while counter < index:
          currentNode = currentNode.next
          counter += 1
        currentNode.prev.next = currentNode.next
        currentNode.next.prev = currentNode.prev
        self.length -= 1
      else:
        currentNode = self.tail
        counter = self.length-1
        while counter > index:
          currentNode = currentNode.prev
          counter -= 1
        currentNode.prev.next = currentNode.next
        currentNode.next.prev = currentNode.prev
        self.length -= 1






myList = LinkedList('100')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.prepend('200')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.append('300')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.insert(1,'350')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.insert(2,'450')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.insert(4,'1')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.insert(6,'2')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.insert(77,'21')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.insert(0,'99')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.insert(1,'111')
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.remove(0)
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.remove(8)
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.remove(2)
myList.printList()
myList.printListReverse()
print("-------------END------------")
myList.remove(3)
myList.printList()
myList.printListReverse()