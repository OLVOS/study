

def make_uniqe(sorted_list):
    if not sorted_list:
        return []

    res = [sorted_list[0]]
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            res.append(sorted_list[i])
    return res

