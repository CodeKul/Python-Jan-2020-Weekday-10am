# Input: [1 2 3 3 3 3 4 5]
# output: [1 2 3 4 5]

def get_uniques(l1):
    uni_l = []
    for no in l1:
        found = False
        for element in uni_l:
            if element == no:
                found = True
                break
        if not found:
            uni_l.append(no)
    return uni_l

l = [1, 2, 3, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5]
u_l = get_uniques(l)
print(u_l)