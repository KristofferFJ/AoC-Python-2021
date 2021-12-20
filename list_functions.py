def flatten_list(nested_lists):
    flat_list = []
    for sub_list in nested_lists:
        for element in sub_list:
            flat_list.append(element)
    return flat_list