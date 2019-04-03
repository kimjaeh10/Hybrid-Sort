from Project3.LinkedList import LinkedList

def merge_lists(lists, threshold):
    """Sort and combine every Linkedlist in lists.
    Use insertion sort when the linkedlist is smaller than or equal to the threshold"""
    last = merge_sort(lists[0], threshold)
    for i in range(1, len(lists)):
        lists[i] = merge(last, merge_sort(lists[i], threshold))
    for elem in lists:
        last = merge(last, elem)
    return last


def merge_sort(linked_list, threshold):
    """Use merge sort to sort the given linkedlist. Return the sorted linked list"""
    if linked_list.length() < 2:
        return linked_list
    elif linked_list.length() <= threshold:
        linked_list.insertion_sort()
        return linked_list
    else:
        split = split_linked_list(linked_list)
        first_tuple = merge_sort(split[0], threshold)
        second_tuple = merge_sort(split[1], threshold)
        return merge(first_tuple, second_tuple)


def split_linked_list(linked_list):
    """Take a Linked list and split it in half
        If the size is odd, split it into size(n/2,n/2+1)
        Returning a tuple of 2 linked lists."""
    list1 = LinkedList()
    list2 = LinkedList()
    length = linked_list.length()
    if linked_list is None:
        return list1, list2

    if length < 2:
        list2.push_back(linked_list.front_value())
        linked_list.pop_front()
    else:
        if length % 2 == 0:
            for i in range(length // 2):
                list1.push_back(linked_list.front_value())
                linked_list.pop_front()
            for i in range(length):
                list2.push_back(linked_list.front_value())
                linked_list.pop_front()
        else:
            for i in range(length // 2):
                list1.push_back(linked_list.front_value())
                linked_list.pop_front()
            for i in range(length):
                list2.push_back(linked_list.front_value() + 1)
                linked_list.pop_front()

    return list1, list2



def merge(list1, list2):
    """Takes in two sorted LinkedLists and merges them together
        Returning one sorted linked list"""
    sorted_list = LinkedList()

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    while list1 and list2:
        data1 = list1.front_value()
        data2 = list2.front_value()
        if data1 <= data2:
            sorted_list.push_back(data1)
            list1.pop_front()
        else:
            sorted_list.push_back(data2)
            list2.pop_front()

    while list1 or list2:
        data1 = list1.front_value()
        data2 = list2.front_value()
        if data1 is None:
            data2 = list2.front_value()
            sorted_list.push_back(data2)
            list2.pop_front()
        if data2 is None:
            data1 = list1.front_value()
            sorted_list.push_back(data1)
            list1.pop_front()

    return sorted_list
