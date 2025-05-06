l = []
def append1(x):
    l.append(x)
    return l
def extend1(l):
    l.extend(l)
    return l
def pop():
    if l:
        return l.pop()
    return "List is empty"
def remove1(x):
    if x in l:
        l.remove(x)
        return l
    return f"{x} not found"
