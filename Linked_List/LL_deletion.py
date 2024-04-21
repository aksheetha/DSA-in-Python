class Node:
  def __init__(self,data):
  self_data = data
  self_next = None

head = Node(10)
node1= Node(20)
node2= Node(30)
node3= Node(40)

#connection
head.next = node1
node1.next = node2
node2.next = node3

#Deletion from the front

if head is not None
head = head.next

#Print
current = head 
while current is not None
  print(current.data, end="--->")
  current = current.next

print("None")

#delete frm end

current = head
while current.next.next is not None
  current = current.next
current.next = None

#delete fron middle
current = head
while curret.next.data != 30
  current = current.next
current.next = curret.next.next

  
