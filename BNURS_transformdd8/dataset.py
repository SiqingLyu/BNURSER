from tools.tools import *
import glob

'''
function:
    first split the data 
    to the original ones and the changed ones
    

usage:
    give the function your input filepath, for an example:
        if your data looks like:
            |trainData
            ||----1_1_label.png
            ||----1_2_label.png
            ||----2_1_label.png
            ||----2_2_label.png
            |gt
            ||----1_change.png
            ||----2_change.png
        then your input should be:
                                    dataprocess('./trainData','./trainData','./gt')
    and you can decide where to put your data_path,origin_path,changed_path,label_path,list_path
    here , I recommand you name the path as
    (and these names are also the default names):
                                                data_path = './BNUDataset'
                                                origin_path = './BNUDataset/A'
                                                changed_path = './BNUDataset/B'
                                                label_path = './BNUDataset/label'
                                                list_path = './BNUDataset/list'
    if you use the naming rules above, you will get a directionary:
        |BNUDataset
        |----A
            ||
            ||   # all the origin imgs
            ||
        |----B
            ||
            ||   # all the changed imgs
            ||
        |----label
            ||
            ||   # all the labels 
            ||
        |----list
            ||----train.txt
            ||----val.txt

data split rules:
    input img name: *_1_label.png
                    *_2_label.png
    output CDimg name: _change.png
    
all the imgs to be trained, their names will be saved in /list/train.txt
the validation imgs comes from the original data,
the function will take a img for validation after saving every 4 imgs
and all the names of validation imgs will be saved in /list/val.txt
'''

def dataprocess(input_path,input_label_path,
                data_path = 'BNUDataset/',origin_path = 'BNUDataset/A/',
                changed_path = 'BNUDataset/B/', label_path = 'BNUDataset/label/', list_path = 'BNUDataset/list/'):
    if os.path.exists(data_path):
      return data_path
    mkdir(data_path)
    mkdir(label_path)
    mkdir(origin_path)
    mkdir(changed_path)
    mkdir(list_path)
    clear(data_path)

    # fns1 = glob.glob(input_1_path+'/*1_label.png')  ##获取当前目录下所有1.png格式的文件
    print(input_path)
    fns1 = glob.glob(input_path+'/*1.png')  ##获取当前目录下所有1.png格式的文件
    for ind in range(len(fns1)):  ##循环移动所有文件
        print(ind)

        my_move(fns1[ind], origin_path)
    # removeSufFix(origin_path,8)  #remove the suffix of the files
    removeSufFix(origin_path,2)
    # fns2 = glob.glob(input_2_path+'/*2_label.png')  ##获取当前目录下所有2.png格式的文件
    fns2 = glob.glob(input_path+'/*2.png')  ##获取当前目录下所有2.png格式的文件

    for ind in range(len(fns2)):

        my_move(fns2[ind], changed_path)
    # removeSufFix(changed_path,8)
    removeSufFix(changed_path,2)

    fns3 = glob.glob(input_label_path+'/*change.png')  ##获取当前目录下所有change.png格式的文件
    for ind in range(len(fns3)):  ##循环移动所有文件

        my_move(fns3[ind], label_path)
    removeSufFix(label_path,7)

    flag = 1
    List1 = []
    List2 = []
    for root, dirs, files in os.walk(origin_path):  # 遍历这个文件夹下每个文件
        for file in files:
            # filename = self.origin_path + file

            filename = file
            if flag % 4 == 0:
                List2.append(filename)
            else:
                List1.append(filename)
            flag += 1
    f = open(list_path+'/train.txt', 'a')  # 没有则创建txt文件，与代码文件同目录
    Str_train = '\n'.join(List1)
    f.write(Str_train)  # png是后缀，根据文件类型修改
    f.close()
    f = open(list_path+'/val.txt', 'a')  # 没有则创建txt文件，与代码文件同目录
    Str_val = '\n'.join(List2)
    f.write(Str_val)  # png是后缀，根据文件类型修改
    f.close()
    return data_path