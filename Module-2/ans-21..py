def reverse_string(a):
    if len(a) % 4 == 0:
        return ''. join(reversed(a))

    return a

print(reverse_string('zara'))
print(reverse_string('kajal'))
