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
  
  # to insert a new beginning node
  # set a new head node or front of the list
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node 
  # new_node -> head_node -> empty
  # new_node = head_node -> empty list -> new_node instead 
    
 # to print out everything in the list 
 # we need to create an empty string to hold all the nodes 
  def stringify_list(self):
    string_list = " "
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
        current_node.get_next_node()
    return string_list
  
  # traverse the node -> start at the head node or front of the list 
  # current node -> head_node
  # if head_node is not empty we can go to the next node aka there needs to be nodes lol
  # take the string of the value of the node: current_node -> str(current_node) -> string_list = "current_node"
  # go to the next value -> the loop stops when you reach null aka end of the list 
  
# test it out 
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())




