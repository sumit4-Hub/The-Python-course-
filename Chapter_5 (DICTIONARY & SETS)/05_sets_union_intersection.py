s1 = {1, 34, 54, 65}
s2 = {1, 44, 64, 25, 87, 34}

print(s1.union(s2))
print(s1.intersection(s2))

print({1, 54}.issubset(s1))
print(s1.issuperset({1, 34}))