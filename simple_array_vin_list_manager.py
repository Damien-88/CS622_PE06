class SimpleArrayVINListManagerClass:

    # Initialize with empty list to store VIN items
    def __init__(self):
        # Create empty list to store VIN items
        self.vin_list = []

    # Insert new item to beginning of list
    def insert_item(self, item):
        # Insert item at index 0 (front of the list)
        self.vin_list.insert(0, item)

    # Print all items in list
    def print_items(self):
        # Print opening
        print("[", end = " ")
        
        # Iterate through each item in list
        for i in self.vin_list:
            # Print current item followed by a space
            print(i, end = " ")

        # Print closing bracket
        print("]")

    # Delete item from the list
    def delete_item(self, item):
        # Try to find and delete the item
        try:
            # Find index of item in list
            index = self.vin_list.index(item)
            # Remove item at found index
            self.vin_list.pop(index)
        # Handle case when item is not found
        except ValueError:
            # Print error message if item doesn't exist
            print("Item not found in the list.")

    # Retrieve last item in list
    def get_last_item(self):
        # Check if list is empty
        if len(self.vin_list) == 0:
            # Return None if empty 
            return None
        
        # Return VIN value of last node
        return self.vin_list[-1]
    
    # Sort list using selection sort algorithm
    def selection_sort(self):
        # Store length of list
        n = len(self.vin_list)

        # Loop through each position in list
        for i in range(n):
            # Assume current position has minimum value
            min_index = i
            # Loop through remaining unsorted elements
            for j in range(i + 1, n):
                # Check if current element is smaller than current minimum
                if self.vin_list[j] < self.vin_list[min_index]:
                    # Update minimum index
                    min_index = j

            # Swap current element with minimum element found
            self.vin_list[i], self.vin_list[min_index] = self.vin_list[min_index], self.vin_list[i]