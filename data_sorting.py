def sort_list_greatest_to_least(list_to_order, counts, ordered_list=None):
    """
    """
    if not ordered_list:
        ordered_list = []
    
    if len(ordered_list) == 25:
        return ordered_list
    
    item = list_to_order[counts.index(max(counts))]

    ordered_list.append(item)

    list_to_order.remove(item)

    counts.remove(max(counts))
    
    return sort_list_greatest_to_least(list_to_order, counts, ordered_list)
