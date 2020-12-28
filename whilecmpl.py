import sys

a = 0
i = int(sys.argv[1])
try:
    at = int(sys.argv[2])
except:
    at = None
print(f'i: ', i, 'at: ', at)
for x in range(1, 11):
    a += i
    i /= 2
    if x == at:
        print(f'x == {at}!\na: ', a, '\ni: ', i, '\n')
    else:
        print(f'a: ', a, '\ni: ', i, '\n')
