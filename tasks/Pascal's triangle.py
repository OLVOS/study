
def triangle(num):
    s = [1]
    while len(s) <= num:
        if num == 0:
            return s

        coll_1 = list(zip([0] + s, s + [0]))
        mapp = map(sum, coll_1)
        s = list(mapp)

    return s


print(triangle(20))
