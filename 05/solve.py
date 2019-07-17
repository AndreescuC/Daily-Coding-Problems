def car(pair):
    def get_first(a, _):
        return a
    return pair(get_first)


def cdr(pair):
    def get_last(_, b):
        return b
    return pair(get_last)
