
els_1 = [True, False, True, True]
els_2 = [True, True, True, True]
els_3 = [False, False, False, False]


print(any(els_1))
print(all(els_1))

print(any(els_2))
print(all(els_2))


people = [15, 17, 21, 24, 18, 19]

print([p >= 18 for p in people])
print(all([p >= 18 for p in people]))
print(any([p < 18 for p in people]))
