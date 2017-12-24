def lazy_num(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

f = lazy_num(1,3,5,7)
print(f())