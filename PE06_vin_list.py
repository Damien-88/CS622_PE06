"""vin_list.py

This assignment is to gain knowledge on Linked List and Selection Sort.
As implementation scenario, vin list have been selected.
The program stores vin items in both of simple array or linked list.
Each storing mechanism are separated to different files such as “simple_array_vin_list_manager.py”
or “linked_list_vin_list_manager.py” each file contains FilenameClass classes with essential methods
for data manipulation. Note that “vin_list.py” with the “main” method have been already implemented,
and you are assigned to implement other classes/methods. As part of assignment, compare actual runtime of
insert/delete/lookup operation between two lists and justify in a short paragraph on how and their performance. 
"""

from simple_array_vin_list_manager import SimpleArrayVINListManagerClass #type: ignore
from linked_list_vin_list_manager import LinkedListVINListManagerClass #type: ignore
# pip install Faker for Faker installation in your computer
from faker import Faker # type: ignore 
import time
import random

# We need to populate the # of items for search operation to compare between simple search and binary search
# total number of samples. Your task is to compare on those 5 values
# N = {10, 100, 1_000, 5_000, 10_000}
# Then analyze the performance between simple search and binary search
N = 10
item_list = [] # empty list for vin items

Faker.seed(0)
fake = Faker()
# store random vin items
for i in range(0, N):
        item_list.append(fake.vin())

def main():
        # Compare how search time varies depending on the position of the target location for deletion
        # target_location = 0 
        # target_location = N//2
        # target_location = N-1 
        target_location = 0
        target_item = item_list[target_location]   

        print("------ Simple array ------")
        sa = SimpleArrayVINListManagerClass()

        #insert operation
        simple_array_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
            sa.insert_item(item_list[i])
        simple_array_insert_end_time = time.perf_counter()

        print("The current list:\t", end = " ")
        sa.print_items()
       
        #delete operation
        simple_array_delete_start_time = time.perf_counter()
        sa.delete_item(target_item)
        simple_array_delete_end_time = time.perf_counter()
        print("Deleted:\t", target_item, end = "\n")        
        sa.print_items()

        #look up operation(last element)
        simple_array_lookup_start_time = time.perf_counter()
        sa_lastElement = sa.get_last_item()
        simple_array_lookup_end_time = time.perf_counter()
        print("Look up the last element:\t%s" % sa_lastElement)
        
        #sort operation
        sa.selection_sort()
        print("Sorted:\t", end = " ")
        sa.print_items()

        #time summary:
        saInsertOp = simple_array_insert_end_time - simple_array_insert_start_time
        saDeleteOp = simple_array_delete_end_time - simple_array_delete_start_time
        saLookupOp = simple_array_lookup_end_time - simple_array_lookup_start_time
        print("-insertion: %.10f\n-deletion: %.10f\n-lookup: %.10f\n" %(saInsertOp, saDeleteOp, saLookupOp))

        print("------ Linked list ------")
        ll = LinkedListVINListManagerClass()
        #insert operation
        linked_list_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
                ll.insert_item(item_list[i])
        linked_list_insert_end_time = time.perf_counter()
 
        print("The current list:\t", end = " ")
        ll.print_items()

        # Compare how search time varies depending on the position of the target location for deletion
        # target_location = 0 
        # target_location = N//2
        # target_location = N-1 

        #delete operation        
        target_location = N//2
        target_item = item_list[target_location]   
                
        linked_list_delete_start_time = time.perf_counter()
        ll.delete_item(target_item)
        linked_list_delete_end_time = time.perf_counter()
        print("Deleted:\t", target_item, end = "\n")
        ll.print_items()
        
        #look up operation(last element)
        linked_list_lookup_start_time = time.perf_counter()
        ll_lastElement = ll.get_last_item()
        linked_list_lookup_end_time = time.perf_counter()
        print("The look up the last element:\t%s" % ll_lastElement)
        
        #sort operation
        ll.selection_sort()
        print("Sorted:\t", end = " ")
        ll.print_items()

        #time summary:
        llInsertOp= linked_list_insert_end_time - linked_list_insert_start_time
        llDeleteOp= linked_list_delete_end_time - linked_list_delete_start_time
        llLookupOp= linked_list_lookup_end_time - linked_list_lookup_start_time
        print("-insertion: %.10f\n-deletion: %.10f\n-lookup: %.10f\n" %(llInsertOp, llDeleteOp, llLookupOp))

if __name__ == "__main__":
        main()