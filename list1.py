lst = []
def append1(x):
    lst.append(x)
    return lst
def extend1(l):
    lst.extend(l)
    return lst
def pop():
    if lst:
        return lst.pop()
    return "List is empty"
def remove1(x):
    if x in lst:
        lst.remove(x)
        return lst
    return f"{x} not found"
