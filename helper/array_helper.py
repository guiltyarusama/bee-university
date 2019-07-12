def get_sublists(original_list, number_of_sub_list_wanted):
    sublists = list()
    # for sub_list_count in range(number_of_sub_list_wanted):
    #     sublists.append(original_list[sub_list_count::number_of_sub_list_wanted])
    # return sublists

    element_size_per_bulk = int(len(original_list) / number_of_sub_list_wanted)
    for i in range(0, len(original_list), element_size_per_bulk):
        # Create an index range for l of n items:
        sublists.append(original_list[i:i + element_size_per_bulk])
    return sublists


# if __name__ == '__main__':
#     print(get_sublists([100, 200, 300, 101, 102, 103, 111, 222, 333, 888], 999))
