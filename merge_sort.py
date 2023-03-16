# merge_sort.py
# Modules for merge sorting algorithm, sorts list passed from merge_main
#
# Usage: python3 merge_main.py filename
# Created - Mark O.P

def merge_sort(random_list, begin, end):
    """ Recursive function for recursive calls for merge_sort

    Parameters
    ----------
    random_list: list
        List you would like to sort
    begin: int
        Initial call should be 0. Beginning of list
    end: int
        Initiall call should be len(list) - 1. End of list

    Returns
    -------
    comparison_count: int
        Sum of merge_sort and merge comparisons
    assignment_count: int
        Sum of merge assignments
    """

    comparison_count = 1
    assignment_count = 0

    if (begin < end):
        middle = (begin + end) // 2
        ms_comparison_count, ms_assignment_count = merge_sort(random_list, begin, middle)
        comparison_count += ms_comparison_count
        assignment_count += ms_assignment_count

        ms_comparison_count, ms_assignment_count = merge_sort(random_list, middle + 1, end)
        comparison_count += ms_comparison_count
        assignment_count += ms_assignment_count

        m_comparison_count, m_assignment_count = merge(random_list, begin, middle, end)
        comparison_count += m_comparison_count
        assignment_count += m_assignment_count

    return comparison_count, assignment_count


def merge(random_list, begin, middle, end):

    """ Helper function for merge_sort, combines the n/2 sublists
    
    Parameters
    ----------
    random_list: list
        List passed from merge_sort, merges halfs
    begin: int
        Beginning index of passed sub-list
    middle: int
        Middle index of passed sub-list
    end: int
        End index of passed sub-list
    
    Returns
    -------
    assignment_count: int
        Number of assignments made in merge
    comparison_count: int
        Number of comparisons made in merge
    """

    assignment_count = 0
    comparison_count = 0

    # left_side (lets us know where left side ends) (begin to left_side)
    left_side = middle - begin + 1
    assignment_count += 1

    # right_side (lets us know where right side begins) (right_side to end)
    right_side = end - middle
    assignment_count += 1

    # initializing empty arrays for left and right sides, need for merging
    left_array = [0] * (left_side + 1)
    right_array = [0] * (right_side + 1)

    
    for i in range (0, left_side):
        assignment_count += 1
        left_array[i] = random_list[begin + i]

    for j in range (0, right_side):
        assignment_count += 1
        right_array[j] = random_list[(middle + 1) + j]

    assignment_count += 1
    left_array[left_side] = float('inf')
    assignment_count += 1
    right_array[right_side] = float('inf')

    assignment_count += 1
    i = 0
    assignment_count += 1
    j = 0

    for k in range (begin, end + 1):

        comparison_count += 1
        if (left_array[i] <= right_array[j]):
            assignment_count += 1
            random_list[k] = left_array[i]
            i = i + 1
        else:
            assignment_count += 1
            random_list[k] = right_array[j]
            j = j + 1

    return comparison_count, assignment_count

