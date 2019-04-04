import os
import shutil

'''
demo功能说明：
在folderPath处新建60个文件夹，
图片存储在path处
给每个文件夹分配150张图片（将9000张图片平均分配到60个文件夹）

Tips:
1: os.path.join(path1,path2...)
this function is used to combine the path,it returns a path which is 'path1/path2...'

2: os.makedirs(path)
this function is used to make a directory(new folder) in the path param

3: shutil.move(oldPath,newPath)
this function is used to move file from param1 to param 2

4: os.path.exists(path)
this function is used to check the filePath(param1) whether exists
'''


class MoveFiles:
    def __init__(self, original_path, target_path, divide_num):
        # original path of files
        self.original_path = original_path
        self.target_path = target_path
        self.divide_num = divide_num
        # original_path = r'D:\v-baoz\label\images\浮世绘和国画\国画'
        # path of target
        # target_path = r'D:\v-baoz\label\images'
        # divide_num = 20

    def mkfolder(self, target_path, divide_num):
        sort_folder_number = [x for x in range(0, divide_num)]
        for number in sort_folder_number:
            new_folder_path = os.path.join(target_path, '{}'.format(number))  # new_folder_path is ‘folderPath\number'
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                print("new a floder named " + str(number) + ' at the path of ' + new_folder_path)
        target_path_list = os.listdir(target_path)
        yield target_path_list

    def get_files_path(self, original_path):
        # get the original abspath
        original_abspath_list = []
        for root, dirs, files in os.walk(original_path):
            single_abspath = os.path.abspath(files)
            original_abspath_list.append(single_abspath)
            yield original_abspath_list
        print('abspath store done')

    def move_files(self, original_path, target_path):
        for original in original_abspath_list:

            if not os.path.exists(new_file_path):
                print('not exist path:' + new_file_path)
                break
            shutil.move(old_file_path, new_file_path)
            print('success move file from ' + old_file_path + ' to ' + new_file_path)

    print('there are ' + str(len(file_list)) + ' files at the path of ' + path)
    for i in range(0, len(file_list)):
        old_file_path = os.path.join(path, file_list[i])
        if os.path.isdir(old_file_path):
            '''if the path is a folder,program will pass it'''
            print('img does not exist ,path=' + old_file_path + ' it is a dir')
            pass
        elif not os.path.exists(old_file_path):
            '''if the path does not exist,program will pass it'''
            print('img does not exist ,path=' + old_file_path)
            pass
        else:
            '''define the number,it decides how many imgs each people process'''
            number = 150  # int(len(file_list)/peopleNumber)
            if (i % number == 0):
                folderNumber += 1
            new_file_path = os.path.join(folderPath, '%s' % (folderNumber))
            if not os.path.exists(new_file_path):
                print('not exist path:' + new_file_path)
                break
            shutil.move(old_file_path, new_file_path)
            print('success move file from ' + old_file_path + ' to ' + new_file_path)
