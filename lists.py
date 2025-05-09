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


def list_of_lists(lists):
    result = []

    # Primera sublista: primeros dos elementos
    if len(lists[0]) >= 2:
        result.append(lists[0][:2])
    else:
        result.append(lists[0])  # Si tiene menos de 2, se agrega lo que haya

    # Segunda sublista: elementos del segundo al cuarto (índices 1 al 3)
    if len(lists[1]) >= 4:
        result.append(lists[1][1:4])
    else:
        result.append(lists[1][1:])  # Si no tiene 4 elementos, hasta donde alcance

    # Tercera sublista: últimos dos elementos
    if len(lists[2]) >= 2:
        result.append(lists[2][-2:])
    else:
        result.append(lists[2])  # Si tiene menos de 2, se agrega lo que haya

    return result
