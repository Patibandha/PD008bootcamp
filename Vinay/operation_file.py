import os


def read_write_op(ab_path, file_name):
    try:

        number = int(input("Enter a number"))
        if number in range(0, 11):
            fil = os.path.join(ab_path, file_name)
            with open(fil, 'w+') as f:
                for i in range(0, 10):
                    f.write("The string is  %d\r\n" % (i + 0))
                    f.write("The output is: ")
                    f.write(str(number))
            f.close()
        else:
            print("invalid input, Please try again", number)


    except ValueError:
        print("invalid statement")


if __name__ == '__main__':
    ab_path = os.path.abspath("Files")
    print(ab_path)
    read_write_op(ab_path, "file01.txt")


