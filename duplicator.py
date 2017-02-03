
def remove_duplicates(arg):
    arga=arg
    arga.sort()
    list_sorted=[arga[0]]
    for i in arga:
        if list_sorted[-1]!=i:
            list_sorted.append(i)
    return list_sorted


def remove_duplicates2(arg):
    arga=arg
    list_sorted=[]
    for i in arg:
        if i not in list_sorted:
            list_sorted.append(i)
    return list_sorted

def remove_duplicates3(arg):
    return list(set(arg))

if __name__ == '__main__':
    import timeit

    a=[4,5,6,2,3,1,2,7,8,2]*1000
    print("My def:   ",timeit.timeit("remove_duplicates(a)", setup="from __main__ import remove_duplicates,a"))
    print("if not in: ",timeit.timeit("remove_duplicates2(a)", setup="from __main__ import remove_duplicates2,a"))
    print("Set:      ",timeit.timeit("remove_duplicates3(a)", setup="from __main__ import remove_duplicates3,a"))
