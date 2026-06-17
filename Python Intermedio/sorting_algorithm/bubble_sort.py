def bubble_sort(sorting_list):
    for outer_index in range (0, len(sorting_list) - 1):
        changes_made = False

        for index in range (0, len(sorting_list)-1):
            current_element = sorting_list[index]
            next_element = sorting_list[index + 1]

            if current_element > next_element:
                sorting_list[index] = next_element
                sorting_list[index + 1] = current_element
                changes_made = True
    
        if not changes_made:
            return


test_list = [10,5,20,6,9]
bubble_sort(test_list)
print(test_list)


