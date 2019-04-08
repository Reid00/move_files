import os


class CountFilesNum:
    def __init__(self, root):
        self.root = root

    def count_num(self):
        count = 0
        for root, dirs, files in os.walk(self.root):
            print('the path {} own files: {}'.format(root, len(files)))
            count = count + len(files)
        print('total number is {}'.format(count))


if __name__ == '__main__':
    count = CountFilesNum(r'D:\v-baoz\test\target')
    count.count_num()
