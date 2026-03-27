from tasks.utils import make_uniqe


def union(nums1, nums2):
    res = []
    f, s = 0, 0

    while f < len(nums1) and s < len(nums2):
        if nums1[f] < nums2[s]:
            res.append(nums1[f])
            f += 1
        elif nums2[s] < nums1[f]:
            res.append(nums2[s])
            s += 1
        elif nums2[s] == nums1[f]:
            res.append(nums1[f])
            s += 1
            f += 1
    return [*res, *nums1[f:], *nums2[s:]]


def uniqe_union(nums1, nums2):
    merge = union(nums1, nums2)
    return make_uniqe(merge)


r = union([1, 1, 1], [1, 2, 2, 2, 2])
print(r)
r = uniqe_union([1, 1, 1], [1, 2, 2, 2, 2])
print(r)

