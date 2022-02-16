import string

ranges = list(map(chr, range(97, 112)))
ranges1 = list(map(chr, range(113, 114)))
ranges2 = list(map(chr, range(116, 123)))
list1 = ranges, ranges1, ranges2


# print(list(map(chr, range(97, 123))))
# print(list(map((chr, range(97, 112)))))
# print(list(map(chr, range(116, 123))))


print(list1)