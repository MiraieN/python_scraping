d = {z: 10-z for z in range(10)}
l = list(d.items())
l.sort(reverse=False)
d = dict(l)
l.sort(reverse=True)
dict = dict(l)
print("ascending order is:", dict)
print("descending order is:", d)
