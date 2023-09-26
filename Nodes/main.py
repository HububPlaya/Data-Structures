# This is how you would implment a node class and instance

# we create a class node that holds some value and link to another node 
class Node:
  def __init__ (self, value, link_node=None): 
    self.value = value
    self.link_node = link_node

# We can access the value and link by creating get methods for both 
  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link_node
  
# We can set new links incase of orphaned nodes by creating a set method for the link_node value 
  def set_link_node(self, link_node):
    self.link_node = link_node

# Otside of the Node class, we can check out method by creating nodes (instances)
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# When we set the links it should looks like this: yacko -> dot -> wacko
dot.set_link_node(wacko)
yacko.set_link_node(dot)

# we check the get values for link and value 
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

# print the results 
print("dots data: " + str(dots_data))
print("wackos data: " + str(wackos_data))
