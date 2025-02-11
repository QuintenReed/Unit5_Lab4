# Quinten Reed
# U5L4
# PositionalDoublyBase

class PositionalDoublyBase():
  class DoublyNode():
    def __init__(self, value):
      self.value = value
      self.next = None
      self.prev = None
    
    def __str__(self):
      """Convert individual node to string"""
      return f"|{self.value}|"

    def set_next(self, value):
      """Sets the next node in the list"""
      if type(value) == type(self) or value == None:
        self.next = value
      else:
        raise TypeError("Needs to be a node")

    def set_prev(self, value):
      """Sets the previous node in the list"""
      if type(value) == type(self) or value == None:
        self.prev = value
      else:
        raise TypeError("Needs to be a node")

  def __init__(self):
    self.header = self.DoublyNode(None)
    self.trailer = self.DoublyNode(None)

    self.header.set_next(self.trailer)
    self.trailer.set_prev(self.header)

    self.__size = 0

  def __str__(self):
    """Convert list to string"""
    out = "HEADER:"

    walk = self.header
    for i in range(self.__size+2):
      out += f"{walk}"
      walk = walk.next
      if walk != None:
        out += " <-> "

    out += ":TRAILER"
    return out

  def __len__(self):
    """Returns length of linked list"""
    return self.__size

  def __is_empty(self):
    """Returns whether the linked list is empty"""
    return self.__size <= 0

  def __insert_between(self, value, pred = False, succ = False):
    """Inserts a new node into the list"""
    if pred == False:
      pred = self.header

    if succ == False:
      succ = self.trailer

    if pred == succ.prev:
      new = self.DoublyNode(value)
      new.set_next(succ)
      new.set_prev(pred)

      pred.set_next(new)
      succ.set_prev(new)

      self.__size += 1
      return new
    else:
      raise IndexError("elements exist between these elements already")

  def __delete_node(self, node):
    """Deletes a node from the list"""
    if node.value != None:
      deleted = node.value

      node.prev.set_next(node.next)
      node.next.set_prev(node.prev)

      node.value = node.prev = node.next = None

      self.__size -= 1
      return deleted
    else:
      raise ValueError("can't delete node with None value (either sentinel or already deleted)")