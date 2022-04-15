import itertools

def next_bigger(n):
    dig_list = [dig for dig in str(n)]
    lengthOfStrings = len(dig_list)
    perm_list = []

    for i in itertools.permutations(dig_list, lengthOfStrings):
        perm_list.append("".join(i))

    perm_list.sort()
    try:
        x = perm_list.index(str(n)) +1
        y = int(perm_list[x])
        if y == n:
            z = perm_list.index(str(n)) +2
            zz = int(perm_list[z])
            return zz
        else: return y
    except:
        return -1