class Node():
  def __init__(self,value):
    self.data = value
    self.next = None

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
    self.length += 1

  def append(self,value):
    prevTailNode = self.tail
    newNode = Node(value) 
    prevTailNode.next = newNode
    self.tail = newNode
    self.length += 1

  def printList(self):
    listArr = []
    currentNode = self.head
    while currentNode is not None:
      listArr.append(currentNode.data)
      currentNode = currentNode.next
    print("Linked List: ", listArr, "& Length: ", self.length)

  def insert(self,index,value):
    if index == 0 :
      self.prepend(value)
    if index >= self.length :
      self.append(value)
    elif index > 0 and index < self.length :
      newNode = Node(value)
      currentNode = self.head
      Idx = 0
      while currentNode is not None:
        if Idx+1 == index:
          oldNode = currentNode.next
          newNode.next = oldNode
          currentNode.next = newNode
          self.length += 1
          break
        currentNode = currentNode.next
        Idx += 1
  
  def remove(self,index):
    if index == 0:
      self.head = self.head.next
      self.length -= 1

    elif index == self.length-1:
      counter = 1
      currentNode = self.head
      while counter < index:
        currentNode = currentNode.next
        counter += 1
      currentNode.next = None
      self.tail = currentNode
      self.length -= 1

    elif index > 0 and index < self.length-1:
      counter = 1
      currentNode = self.head
      while counter < index:
        currentNode = currentNode.next
        counter += 1
      print(currentNode)
      currentNode.next = currentNode.next.next
      self.length -= 1






myList = LinkedList('100')
myList.printList()
print("-------------END------------")
myList.prepend('200')
myList.printList()
print("-------------END------------")
myList.append('300')
myList.printList()
print("-------------END------------")
myList.insert(1,'350')
myList.printList()
print("-------------END------------")
myList.insert(2,'450')
myList.printList()
print("-------------END------------")
myList.insert(4,'1')
myList.printList()
print("-------------END------------")
myList.insert(6,'2')
myList.printList()
print("-------------END------------")
myList.insert(77,'21')
myList.printList()
print("-------------END------------")
myList.insert(0,'99')
myList.printList()
print("-------------END------------")
myList.insert(1,'111')
myList.printList()
print("-------------END------------")
myList.remove(0)
myList.printList()
print("-------------END------------")
myList.remove(8)
myList.printList()
print("-------------END------------")
myList.remove(2)
myList.printList()
print("-------------END------------")
myList.remove(6)
myList.printList()
print("-------------END------------")
myList.remove(4)
myList.printList()