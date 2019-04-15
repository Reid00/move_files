import os
import re


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
    count = CountFilesNum(r'C:\Users\v-baoz\OneDrive\editPicatureFinished-MS-201705171604\浮世绘')
    count.count_num()
