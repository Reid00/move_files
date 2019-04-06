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

    def mkdirs(self):
        sort_folder_number = [x for x in range(0, int(self.divide_num))]
        for number in sort_folder_number:
            new_folder_path = os.path.join(self.target_path,
                                           '{}'.format(number))  # new_folder_path is ‘folderPath\number'
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                print("new a floder named " + str(number) + ' at the path of ' + new_folder_path)
        for root, dirs, files in os.walk(self.target_path):
            target_path_list = [os.path.abspath(os.path.join(self.target_path, dir)) for dir in dirs]
            # target_path_list = [os.path.join(self.target_path, foldername) for foldername in os.listdir(self.target_path)]
            if target_path_list:
                print(target_path_list)
                print('target_path_list print done')
                return target_path_list

    def get_default_path(self):
        # get the original abspath
        original_abspath_list = []
        for root, dirs, files in os.walk(self.original_path):
            original_abspath_list = [os.path.join(root, file) for file in files]
            print(original_abspath_list)
        print('abspath store done')
        return original_abspath_list

    def move_files(self, original_abspath_list, target_path_list):
        for i in range(self.divide_num):
            if not os.path.exists(target_path_list[i]):
                print('not exist path:' + target_path_list[i])
                break
            number = int(len(original_abspath_list)) / int(self.divide_num)
            for item in range(int(i * number), int(i * number + number)):
                if not os.path.exists(original_abspath_list[item]):
                    print('original path not exist files: ' + original_abspath_list[item])
                    continue
                shutil.move(original_abspath_list[item], target_path_list[i])
                print('success move file from ' + original_abspath_list[item] + ' to ' + target_path_list[i])


if __name__ == '__main__':
    test = MoveFiles(r'D:\v-baoz\test\original', r'D:\v-baoz\test\target', 10)
    target_path_list = test.mkdirs()
    original_abspath_list = test.get_default_path()
    test.move_files(original_abspath_list, target_path_list)
