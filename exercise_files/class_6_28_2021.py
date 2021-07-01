# Data type in Python
"""
1) strings (index, mutable)
2) numbers (mutable)
3) list (index, , mutable) array
4) tuple (index, immutable)
5) dictionary
6) set (index)

TDD Test Driven Development
"""


def data_type(*args, **kwargs):  # <somename_<someanother name>> no caps str, list,
    name = args[0][0:8:]  # Python slicing
    # name_with_last_namame = kwargs
    print(name[::-1])
    # print(name_with_last_name)
    # for i in name:
    #     print(i)

    # for j in range(0, 12):
    #     print(args[0][j])
    # return name
    #
    # # Numbers
    # num = args[1]
    # # print(num)
    #
    # # list
    # ls = args[3][0:3]
    # # print(ls)
    #
    # # tuple
    #
    # tp = args[4][0:2]
    # # print(tp)
    # # settt = set(args[5])
    #
    # ls.append("this is append works")
    #
    # # print(tp)

    # dictionary
    # kw = {}
    # for key, value in kwargs.items():
    #     print(key, value)
    #     kw.update({key: value})
    # # print(kw)
    #
    # return kw


# data_type(meet=33, dev=19, vinay=22)
# print(output)

data_type(
    "Shailija77&&&(99OOI093920--",  # 0
    #01234567
   #(87654321)
    45.22,                          # 1
    "HELLO",                        # 2
    ["dev", 2021, "Awesome", [0, 0, 7], 2021],  # 3
    ("Shilja", 2021, "Awesome!!!"),  # 4
    ["dev", "Awesome", [0, 0, 7]],   # 5
),
# 6
#  key # value
# [val1:val2:val3]
# val1: intitation of the index value object
# val2: end of index of index value object (till when number (exclude provided number))
# val3: provide value to access index value object e.g. -1 reverse the string
