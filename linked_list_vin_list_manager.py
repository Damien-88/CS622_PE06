class LinkedListVINListManagerClass:
    
    # Initialize linked list with no head node
    def __init__(self):
        # Set head pointer to None, indicating an empty list
        self.head = None

    # Define Node class to represent each element in linked list
    class Node:
        # Initialize node with VIN value
        def __init__(self, vin):
            # Store VIN value
            self.vin = vin
            # Set next pointer to None initially
            self.next = None

    # Insert new item at beginning of linked list
    def insert_item(self, item):
        # Create new node with given item
        new_node = self.Node(item)
        # Link new node to current head
        new_node.next = self.head
        # Update head to point to new node
        self.head = new_node

    # Print all items in linked list
    def print_items(self):
        # Start from head of list
        current_node = self.head
        # Print opening bracket
        print("[", end = " ")

        # Traverse linked list
        while current_node:
            # Print current node's VIN value
            print(current_node.vin, end = " ")
            # Move to next node
            current_node = current_node.next
        
        # Print closing bracket
        print("]")
    
    # Delete an item from linked list
    def delete_item(self, item):
        # Start from head of list
        current_node = self.head
        # Initialize previous node tracker to None
        previous_node = None

        # Traverse list to find item
        while current_node:
            # Check if current node contains item to delete
            if current_node.vin == item:
                # If previous node exists, link it to node after current
                if previous_node:
                    previous_node.next = current_node.next
                # If no previous node, update head to skip the current node
                else:
                    self.head = current_node.next
        
                # Exit function after deletion
                return
        
            # Move previous pointer to current node
            previous_node = current_node
            # Move current pointer to next node
            current_node = current_node.next
        
        # Print message if item was not found
        print("Item not found in the list.")

    # Retrieve last item in linked list
    def get_last_item(self):
        # Check if list is empty
        if not self.head:
            # Return None if empty
            return None
        
        # Start from head
        current_node = self.head
        
        # Traverse until last node
        while current_node.next:
            # Move to next node
            current_node = current_node.next
        
        # Return VIN value of last node
        return current_node.vin
    
    # Find node with smallest VIN value starting from a given node
    def find_smallest(self, node):
        # Check if node is None
        if not node:
            # Return None if starting node is empty
            return None
        
        # Initialize smallest value with current node's VIN
        smallest = node.vin
        # Initialize smallest node reference to current node
        smallest_node = node
        # Start traversal from given node
        current_node = node 

        # Traverse through all remaining nodes
        while current_node:
            # Compare current node's VIN with smallest found so far
            if current_node.vin < smallest:
                # Update smallest value if smaller is found
                smallest = current_node.vin
                # Update smallest node reference
                smallest_node = current_node
            
            # Move to next node
            current_node = current_node.next

        # Return node with smallest VIN value
        return smallest_node
    
    # Sort linked list using selection sort algorithm
    def selection_sort(self):
        # Start from head of list
        current_node = self.head

        # Traverse through each node in list
        while current_node:
            # Find smallest node from current position onwards
            smallest_node = self.find_smallest(current_node)

            # Check if smallest node is different from current node
            if smallest_node != current_node:
                # Swap VIN values between current and smallest nodes
                current_node.vin, smallest_node.vin = smallest_node.vin, current_node.vin
            
            # Move to next node
            current_node = current_node.next