# A linked list is a data structure that contains a chain of nodes connecting in a single direction 
# common operation for linked list: adding, removing, finding, and trasvering through nodes 

# EX node:a -> node:b -> node:c -> null 
# the linked list containes 3 nodes that end at node c 

# how would we remove a node

# EX a -> b -> c -> d -> e -> null
# remove c
# link b -> d 
# then remove c output: a -> b -> d -> e -> null

# the head node is the front of the list 


# Define your Node class below:

# instead of link_node, we need to use next_node to move through the list 
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node 

  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node 
  
  def set_next_node(self, next_node):
    self.next_node = next_node 
  
# my_node = Node(44)
# print(my_node.get_value())

# the linked list class containes the head node and how to extract the head node 
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  # to insert a new head
  def set_head_node(value):
    return ""
 # to print out everything in the list 



