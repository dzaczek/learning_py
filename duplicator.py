
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


if __name__ == '__main__':
    import timeit

    a=[4,5,5,3,2,3,2,1,2,3,2,3,1,2,3,4,2,1,2,3,4,5,2,1,23,4,21,3,3,2,1,2,3,4,5,6,4,5,6,4]*25
    print(timeit.timeit("remove_duplicates(a)", setup="from __main__ import remove_duplicates,a"))
    print(timeit.timeit("remove_duplicates2(a)", setup="from __main__ import remove_duplicates2,a"))
