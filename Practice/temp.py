
def arrfunc():
    arr = [1,7,6,8]
    arrFrom = [1,7,2]
    arrTo = [2,9,5]
    s = set()
    for i in arr:
        s.add(i)

    for i in range(len(arrFrom)):

        if arrFrom[i] in s:
            s.remove(arrFrom[i])
            s.add(arrTo[i])

    l = list(s)
    l.sort()

    print(l)



def register():
    pass


def login():

    pass


