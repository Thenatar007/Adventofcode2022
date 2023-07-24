import fileinput
array = []
array2=[]
points= 0
counter = 0
var1 = 0
var2 = 1
var3 = 2
var4 = 3


from collections import defaultdict
from itertools import accumulate


dirs = defaultdict(int)

for line in open('adventinput7.txt'):
    match line.split():
        case '$', 'cd', '/': curr = ['/']
        case '$', 'cd', '..': curr.pop()
        case '$', 'cd', x: curr.append(x+'/')
        case '$', 'ls': pass
        case 'dir', _: pass
        case size, _:
            for p in accumulate(curr):
                dirs[p] += int(size)

print(sum(s for s in dirs.values() if s <= 100_000),
      min(s for s in dirs.values() if s >= dirs['/'] - 40_000_000))
