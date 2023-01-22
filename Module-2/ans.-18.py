s = 'dog'
a = 'crying'
if len(s) > 2:
    if s.endswith('ing'):
        s += 'ly'
    else:
        s += 'ing'
print(s)

if len(a) > 2:
    if a.endswith('ing'):
        a += 'ly'
    else:
        a += 'ing'
print(a)