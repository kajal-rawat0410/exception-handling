s= set()
def slen2():
    return len(s)
def adds2(x):
    s.add(x)
    return s
def remove2(x):
    if x in s:
        s.remove(x)
        return s
    return f"{x} not found in set"
