class DLLIterator:
    def __init__(self, start, trailer):
        self.current = start
        self.trailer = trailer

    def __next__(self):
        if self.current is self.trailer:
            raise StopIteration("No more values.")
        else:
            return_value = self.current.value
            self.current = self.current.next
            return return_value
    
    def __iter__(self):
        return self

#Class: Node
class Node:
    def __init__(self, v, p, n):
        """
            Description of Function:
                initializes an empty node
            Parameters:
                v: value of node
                p: reference to prev node
                n: reference to next node
            Return:
                None
        """
        self.value = v
        self.prev = p
        self.next = n

    def __str__(self):
        """
            Description of Function: 
                returns a string representing the node
            Parameters: 
                None
            Return: 
                str
        """
        return str(self.value)

#Class: DoublyLinkedList 
class DoublyLinkedList:
    def __init__(self):
        """
            Description of Function:
                initializes an empty list
            Parameters:
                None
            Return:
                None
        """
        self.header = Node(None, None, None)
        self.trailer = Node(None, self.header, None)
        self.header.next = self.trailer
        self.size = 0

    def __str__(self):
        """
            Description of Function: 
                returns a string representing the list
            Parameters: 
                None
            Return: 
                str
        """
        #handle empty list case
        if self.header.next.value is None:
            return '[]'
        
        result = '['
        #create a reference to the first value in list
        temp_node = self.header.next

        #stop before the trailer so we don't add an extra space
        while temp_node.next.value is not None:
            result += str(temp_node) + " "
            temp_node = temp_node.next
        
        return result + str(temp_node) + ']'
    
    def __iter__(self):
        return DLLIterator(self.header.next, self.trailer)

    def is_empty(self):
        """
            Description of Function: 
                returns True if the list is empty, False otherwise
            Parameters: 
                None
            Return: 
                bool
        """
        return self.header.next is self.trailer

    def get_size(self):
        """
            Description of Function: 
                returns the size of the list
            Parameters: 
                None
            Return: 
                int
        """
        return self.size

    def add_between(self, v, n1, n2):
        """
            Description of Function: 
                adds value v between n1 and n2
            Parameters:
                v: type is the generic type E of the list
                n1: node in list
                n2: second node in list
            Return: 
                None
        """
        #checks if n1 or n2 is None
        if n1 is None or n2 is None:
            raise ValueError("Invaild n1 or n2 - can't be None.")
        
        #checks if n1 and n2 are not next to each other
        if n1.next is not n2:
            raise ValueError("Second node must come before first node")
        
        #step 1: make a new node
        new_node = Node(v, n1, n2)

        #step 2: fix n1.next and n2.prev
        n1.next = new_node
        n2.prev = new_node

        #step 3: increment sixe
        self.size += 1
    
    def remove_between(self, node1, node2):
        """
            Description of Function: 
                removes and returns value of node between n1 and n2
                there can only be one node between n1 and n2
            Parameters:
                n1: node in list
                n2: second node list
            Return: 
                int
        """
        # check if either node1 or node2 is None. Raise a ValueError if so.
        if node1 is None or node2 is None:
            raise ValueError("Invaild node1 or node2 - can't be None.")
        
        # Check that node1 and node 2 has exactly 1 node between them
        # raise a ValueError if not
        elif node1.next.next is not node2 and node2.prev.prev is not node1:
            raise ValueError("There is not only one node between node1 and node2.")

        else:
            #step 1: store the value being removed
            return_value = node1.next.value

            #step 2: delete the node by removing the references to it
            node1.next = node2
            node2.prev = node1
            
            #step 3: decrement size
            self.size -= 1

            #step 4: return the value
            return return_value

    def add_first(self, v):
        """
            Description of Function: 
                adds a the value v at the head of the list
            Parameters:
                v: type is the generic type E of the list
            Return:
                None
        """
        self.add_between(v, self.header, self.header.next)

    def add_last(self, v):
        """
            Description of Function:
                adds a the value v at the tail of the list
            Parameters:
                v: type is the generic type E of the list
            Return:
                None
        """
        self.add_between(v, self.trailer.prev, self.trailer)

    def remove_first(self):
        """
            Description of Function:
                removes and returns the first value in the list
            Parameters:
                None
            Return:
                None
        """
        return self.remove_between(self.header, self.header.next.next)

    def remove_last(self):
        """
            Description of Function:
                removes and returns the last value in the list
            Parameters:
                None
            Return:
                None
        """
        return self.remove_between(self.trailer.prev.prev, self.trailer)
    
    def first(self):
        """
            Description of Function:
                returns the first value in the list
            Parameters:
                None
            Return:
                int
        """
        return self.header.next.value

    def last(self):
        """
            Description of Function:
                returns the last value in the list
            Parameters:
                None
            Return:
                int
        """
        return self.trailer.prev.value

    def search(self, value):
        """
            Description of Function:
                returns the index of the value if found and -1 otherwise
            Parameters:
                value: int value being searched for in the list
            Return:
                int
        """
        #variable to track index
        index = 0

        #set a temporary node to the first value in the list
        temp_node = self.header.next

        #iterate through list until value is reached, then return index
        while temp_node.value is not None:
            if temp_node.value == value:
                return index
            else:
                index += 1
                temp_node = temp_node.next
        #if the value is not found, return -1
        return -1
    
    def get(self, index):
        """
            Description of Function:
                returns the value at index i
            Parameters:
                i: the index
            Return:
                int
        """
        #IndexError
        if index >= self.size:
            raise IndexError("Index is out of range.")
        
        #step 1: create variable to track the index
        idx_value = 0

        #step 2: create a second variable to traverse the list 
        temp_node = self.header.next

        #step 3: traverse list until the given index and return value
        while True:
            if idx_value == index:
                return temp_node.value
            temp_node = temp_node.next
            idx_value += 1
    
    def remove_value(self, value):
        """
            Description of Function:
                searches the list for a value:
                if the value is found, removes it and returns the value
            Parameters:
                value: the value being searched for
            Return:
                None
        """
        temp_node = self.header.next

        #iterate through the list until value is found
        while temp_node.value is not self.trailer and temp_node.value != value:
            temp_node = temp_node.next

        if temp_node is self.trailer:
            return None

        return self.remove_between(temp_node.prev, temp_node.next)

# def homework_driver():
#     test_list = DoublyLinkedList()
#     random.seed(3)
#     for i in range(10):
#         test_list.add_last(random.randint(0, 9))
#     search = random.randint(0, 9)
#     print(test_list.search(search))  
# homework_driver()

#test code! <3
# l = DoublyLinkedList()
# print(l)

# l.add_first([5, 2])
# l.add_last(6)

# for value in l:
#     print(value)

# def dll_tester():
#     # create a DoublyLinkedList
#     test_list = DoublyLinkedList()
    
#     #testing list creation
#     assert test_list.get_size()==0,   'list should be empty to start!'
    
#     #testing add_first
#     test_list.add_first(1)
#     assert test_list.first() == 1, 'add_first needs adjustment!'
#     assert test_list.last() == 1, 'add_first needs adjustment!'
#     assert test_list.get_size() == 1 ,    'add_first needs adjustment!'
#     test_list.add_first(2)
#     assert test_list.first() == 2, 'add_first needs adjustment!'
#     assert test_list.last() == 1, 'add_first needs adjustment!'
#     assert test_list.get_size() == 2, 'add_first needs adjustment!'
    
#     #testing add_last
#     test_list.add_last(3)
#     assert test_list.first() == 2,'add_last needs adjustment!'
#     assert test_list.last() == 3, 'add_last needs adjustment!'
#     assert test_list.get_size() == 3, 'add_last needs adjustment!'

#     #test remove_first
#     assert test_list.remove_first() == 2, 'remove_first needs adjustment!'
#     assert test_list.first() == 1, 'remove_first needs adjustment!'
#     assert test_list.last() == 3, 'remove_first needs adjustment!'
#     assert test_list.get_size() == 2, 'remove_first needs adjustment!'

#     #test remove_last
#     assert test_list.remove_last() == 3, 'remove_last needs adjustment!'
#     assert test_list.first() == 1, 'remove_last needs adjustment!'
#     assert test_list.last() == 1, 'remove_last needs adjustment!'
#     assert test_list.get_size() == 1, 'remove_last needs adjustment!'

#     while not test_list.is_empty():
#         test_list.remove_first()

#     assert test_list.get_size() == 0, 'list should be empty after removing all values'    

#     for i in range(10):
#         test_list.add_last(i+1)
#     #test get method
#     assert test_list.get(0) == 1, 'get(0) should return the element at first index'
#     assert test_list.get(5) == 6, 'get(1) should return the element at index 1'
#     assert test_list.get(9) == 10, 'get(9) should return the element at last index'

#     print('All tests passed!')

# dll_tester()
