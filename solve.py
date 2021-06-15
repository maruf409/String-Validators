n = input()
i = None
j = None
k = None
l = None
m = None

for x in n:
    if x.isalnum():
        i = 1

for y in n:
    if y.isalpha():
        j = 1

for z in n:
    if z.isdigit():
        k = 1

for v in n:
    if v.isupper():
        l = 1

for r in n:
    if r.islower():
        m = 1

if i == 1:
    print(True)
else:
    print(False)

if j == 1:
    print(True)
else:
    print(False)

if k == 1:
    print(True)
else:
    print(False)

if m == 1:
    print(True)
else:
    print(False)


if l == 1:
    print(True)
else:
    print(False)
