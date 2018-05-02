"""
Find the duplicates in the array
"""
dups = [4,7,2,9,4,87,5,45,3,5,45,7,8,9,4]

def dup_guard(arr):
    """
    This is Big O = N 
    Alternate: Sort and then find which would be BigO (N Log N)
    """
    scanned = []
    dup = []
    for n in dups:
        if n not in scanned:
            scanned.append(n)
        else:
            dup.append(n)

    return set(dup)

checkdp = dup_guard(dups)
print(checkdp)

