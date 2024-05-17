# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    x=len(list_to_remove_elements)
    if x>1:
        del list_to_remove_elements[0]
    if x==5:
        del list_to_remove_elements[3]
    if x>5:
        del list_to_remove_elements[3]
        del list_to_remove_elements[3]
        
    
    return list_to_remove_elements


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,'Pink')
    list_to_add_elements.insert(len(list_to_add_elements), 'Yellow')
    return list_to_add_elements


def is_empty(list_to_check):
    x=len(list_to_check)
    return x==0
    

def check_lists(list_to_compare1, list_to_compare2):
    x=len(list_to_compare1)
    y=len(list_to_compare2)
    if x>=3 and y>=3:
        return list_to_compare1[2]==list_to_compare2[2]
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    lista1=list_of_lists_to_modify[0][:2]
    lista2=list_of_lists_to_modify[1][1:4]
    lista3=list_of_lists_to_modify[2][2:]
    
    return [lista1,lista2,lista3]
    
    
    
