class Node:
	def __init__(self, data=None):
		self.next = None 
		self.data = data
		self.position = None 


class LinkedList:
	"""
	Class to manage insertion, deletion and search for Linked List
	"""

	def __init__(self, node):
		self.start = node
		node.next = None 
		self.count = 1
		

	def add(self, new_node):
		node = self.start
		while node.next != None:
			node = node.next

		# node now points to the last
		node.next = new_node
		self.count = self.count + 1
		node.position = self.count

	def insert_at(self, new_node,pos=None):
		if pos < 0 or pos > self.count:
			raise ValueError("Incorrect position. Cannot be greater than count")
		
		prev = self.find_pos(pos=pos-1)
		print("FOUND",prev.data)
		next_node = prev.next 
		prev.next = new_node
		new_node.next = next_node
		self.count = self.count + 1		 
		
	def find_pos(self, pos=None):
		""" Given a position returns the previous and adjacent node """

		if pos < 0 or pos > self.count:
			raise ValueError("Incorrect position. Cannot be greater than count")
		node = self.start
		count = 0
		found = None 

		while node != None:
			if count == (pos):
				found = node
				break
			node = node.next
		return found

	def find_previous(self, findnode):
		node = self.start
		while node != None:
			prev = node 
			node = node.next 
			if node == findnode:
				return prev 
		return None 


	def delete(self, node_del):
		if node_del.next is None:
			# deleting the last node
			after = None 
		else:
			after = node_del.next 
		prev = self.find_previous(node_del)
		prev.next = after
		node_del = None 


	@property
	def get_count(self):
		return self.length

	def list_values(self):
		node = self.start
		while node != None:
			print(node.data)
			node = node.next 

if __name__ == '__main__':
	start = Node(data={"name": "Node0", "city": "brooklyn"})
	linked_list = LinkedList(start)
	node_2 = Node(data={"name": "Node1", "city": "Valeria"})
	node_3 = Node(data={"name": "Node2", "city": "Khor"})

	linked_list.add(node_2)
	linked_list.add(node_3)
		
	new_node = Node(data={"name": "Node2new", "city": "Zabar"})
	linked_list.insert_at(new_node,pos=1)

	linked_list.list_values()

	linked_list.delete(node_3)
	print("============\n")
	linked_list.list_values()

