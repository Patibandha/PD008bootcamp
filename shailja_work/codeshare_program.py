def length_of_string(my_string):
    sub_string = ''
    max_length = 0

    for i in my_string:
        if i not in sub_string:
            sub_string += i
            print(sub_string,"sub string")
            max_length = max(max_length, len(sub_string))
            print(max_length,"maximum length")
        else:
            change = sub_string.index(i)
            print(change)
            sub_string = sub_string[change + 1:] + i
            print(sub_string,"final sub string")
    return max_length


if __name__ == '__main__':

    print(length_of_string("abcabcbb"))
    print()
