L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
## 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0]

print(sorted(L,key=by_name))

### 再按成绩从高到低排序：重点是从高到低
def by_score(t):
    return t[1]*-1

print(sorted(L,key=by_score))