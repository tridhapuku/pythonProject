import roman

def foo(x):
    n, r = x.split()
    return n, roman.fromRoman(r)

def sortRoman(names):
    ans = sorted(set(names) , key=foo)
    return ans

names = ['Louis IX', 'Louis VIII', 'Maria III', 'Oscar IV', 'Adams XXX', 'Anuar III', 'Maria III', 'Oscar V']
# names = sorted(set(names), key=foo)
ans = sortRoman(names)
print(ans)