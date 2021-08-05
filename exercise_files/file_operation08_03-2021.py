"""
This is file operation exercises
"""
import os


def read_write_op(ab_path, file_name):
    fil = os.path.join(ab_path, file_name)
    with open(fil, 'w+') as f:
        f.write("This is Awesome file\n")
        f.write("This is not my file, but I like to have it!")


if __name__ == '__main__':
    ab_path = os.path.abspath("my_files")
    print(ab_path)
    read_write_op(ab_path,"file01.txt")


