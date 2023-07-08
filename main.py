import os


def read_file(file):
    f = open(file, "r")
    f1 = f.read()
    print(f1)
    f.close()


def append_file(file):
    temp = input("Enter new string you want in the file: ")
    f = open(file, 'a')
    f1 = f.write('\n' + temp)
    f.close()


def copy_file(file):
    f = open(file, 'r')
    f1 = open('data_copy.txt', 'x')
    f2 = f1.write(f.read())
    f.close()
    f1.close()


def delete_file(file):
    os.remove(file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file("data.txt")
    copy_file("data.txt")
    read_file("data_copy.txt")
    delete_file("data_copy.txt")
    read_file("data_copy.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
