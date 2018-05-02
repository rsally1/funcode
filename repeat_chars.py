""" 
Find repeat characters in this string.
Ignore whitespace
"""

def find_dups():
    sentence = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    dups = []
    scanned = []
    for s in sentence:
        if s not in scanned:
            scanned.append(s)
        else:
            if s != " " and s != "," and s != ".":
                dups.append(s)
    dups.sort()
    return dups

res = find_dups()
print(res)

def remove_dups():
    sentence = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    res = set(sentence)
    
    return res 


res = remove_dups()
print(res)
