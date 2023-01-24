
def FindMax(lst):
    """return the maximum element"""

    current_max = lst[0]

    for i in (lst):
        if lst[i] > current_max:
            current_max = lst[i]

    return current_max

test_list = [17*i % 2023 for i in range(10000)]

print(FindMax(test_list))
