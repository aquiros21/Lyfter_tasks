def bubble_sort(sorting_list):
    for outer_index in range(0, len(sorting_list) - 1): # O(n)
        changes_made = False # O(1)
        for index in range(0, len(sorting_list) - 1): # O(n)
            current_element = sorting_list[index] # O(1)
            next_element = sorting_list[index + 1] # O(1)
            if current_element > next_element: # O(1)
                sorting_list[index] = next_element # O(1)
                sorting_list[index + 1] = current_element # O(1)
                changes_made = True # O(1)
        if not changes_made: # O(1)
            return # O(1)


def bubble_sort_right_to_left(sorting_list):
    for outer_index in range(0, len(sorting_list) - 1): # O(n)
        changes_made = False # O(1)
        for index in range(len(sorting_list) - 1, 0, -1): # O(n)
            current_element = sorting_list[index] # O(1)
            prev_element = sorting_list[index - 1] # O(1)
            if current_element < prev_element: # O(1)
                sorting_list[index] = prev_element # O(1)
                sorting_list[index - 1] = current_element # O(1)
                changes_made = True # O(1)
        if not changes_made:# O(1)
            return # O(1)


def print_numbers_times_2(numbers_list): 
	for number in numbers_list: # O(n)
		print(number * 2) # O(1)


def check_if_lists_have_an_equal(list_a, list_b): 
	for element_a in list_a: # O(n)
		for element_b in list_b: # O(m)
			if element_a == element_b: # O(1)
				return True # O(1)
				
	return False # O(1)


def print_10_or_less_elements(list_to_print): 
	list_len = len(list_to_print) # O(1)
	for index in range(min(list_len, 10)): # O(1)
		print(list_to_print[index]) # O(1)


def generate_list_trios(list_a, list_b, list_c): 
	result_list = [] # O(1)
	for element_a in list_a: # O(n)
		for element_b in list_b: # O(n)
			for element_c in list_c: # O(n)
				result_list.append(f'{element_a} {element_b} {element_c}') # O(1)
				
	return result_list  # O(1)


