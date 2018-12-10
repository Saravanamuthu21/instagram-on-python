import itertools

password = raw_input("enter the combination:")

result = itertools.permutations(password)

for item in result:
    print ''.join(list(item))