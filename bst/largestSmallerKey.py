"""
Returns the largest node smaller than the passed-in key. If no such node exists
(i.e. when the key is smaller than the smallest node in the tree) then the
function returns -1.
"""

class Node:

# Constructor to create a new node
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None

class BinarySearchTree:

  def __init__(self):
      self.root = None

  def find_largest_smaller_key(self, num):
    return self.helper(self.root, num)
    
  def helper(self, node, num, bestSoFar=None):
    if node is None:
      # print bestSoFar
      return bestSoFar
    
    if num < node.key:
      return self.helper(node.left, num, bestSoFar)
    else:
      bestSoFar = node.key
      return self.helper(node.right, num, bestSoFar)
    

  # THIS INSERT CODE WAS BORROWED FROM THE INTERNET
  def insert(self, key):

      # 1) If tree is empty, create the root
      if (self.root is None):
          self.root = Node(key)
          return

      # 2) Otherwise, create a node with the key
      #    and traverse down the tree to find where to
      #    to insert the new node
      currentNode = self.root
      newNode = Node(key)

      while(currentNode is not None):
        if(key < currentNode.key):
          if(currentNode.left is None):
            currentNode.left = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.left
        else:
          if(currentNode.right is None):
            currentNode.right = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.right

######################################### 
# Driver program to test above function #
#########################################

bst  = BinarySearchTree()
 
# Create the tree given in the above diagram 
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

result = bst.find_largest_smaller_key(17)

print ("Largest smaller number is %d " %(result))
