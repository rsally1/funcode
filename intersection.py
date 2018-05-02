"""
Find the intersection between two arrays
"""
# solution 1: Treating them like sets
a = [21,34,41,22,35]
b = [61,34,45,21,11]
aa = set(a)
bb = set(b)
print(aa.intersection(bb))

# can also be done by looping
found = []
for i in a:
    if i in a and i in b:
        found.append(i)
print(found)
