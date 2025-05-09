# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    list_to_remove = list_to_remove_elements
    if len(list_to_remove) == 6:
        del list_to_remove [5]
        del list_to_remove [4]
        del list_to_remove [0]
    elif len(list_to_remove) == 4:
        del list_to_remove [0]
    else: 
        list_to_remove = []
    return(list_to_remove_elements)  # Remove this line and implement


def add_elements(list_to_add_elements):
    list_add_elements = list_to_add_elements
    if len(list_add_elements) == 4:
        list_add_elements.insert(0, "Pink")
        list_add_elements.append("Yellow")
    elif list_add_elements == []:
        list_add_elements.insert(0, "Pink")
        list_add_elements.append("Yellow")
    else:
        list_add_elements.insert(0, "Pink")
        list_add_elements.append("Yellow")
    return(list_to_add_elements)  # Remove this line and implement


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else: 
        return False # Remove this line and implement


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >=3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
 # Remove this line and implement


def list_of_lists(list_of_lists_to_modify):
    list_one = list_of_lists_to_modify[0]
    list_two = list_of_lists_to_modify[1]
    list_three = list_of_lists_to_modify[2]

    if len(list_one) > 2:
        list_one_new = [list_one[0], list_one[1]]
    else:
        list_one_new = list_one

    len2 = len(list_two)
    if len2 == 2:
        list_two_new = [list_two[1]]
    elif len2 == 3:
        list_two_new = [list_two[1], list_two[2]]
    elif len2 >= 4:
        list_two_new = [list_two[1], list_two[2], list_two[3]]
    else: 
        list_three_new = []
    return (list_of_lists_to_modify) # Remove this line and implement
