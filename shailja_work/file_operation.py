import os


def read_write_op(ab_path, file_name):
    fil = os.path.join(ab_path, file_name)
    with open(fil, 'w+') as f:
        for i in range(0, 10):
            f.write("The line number %d\r\n" %(i + 0))


if __name__ == '__main__':
    ab_path = os.path.abspath("my_files1")
    print(ab_path)
    read_write_op(ab_path,"file_test1.txt")
