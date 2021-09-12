#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''

image process tools

use for making directionary and moving files

'''

import os
import shutil

def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        # print path+'创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print path+' 目录已存在'
        return False


def my_move(srcfn, dstdir):  ##定义移动函数，参数为待移动的文件路径和目标目录
    if not os.path.isfile(srcfn):  ##判断文件是否存在
        print('srcfn error')

    else:
        srcdir, fn = os.path.split(srcfn)  ##分离绝对路径和相对路径，获得文件名

        if not os.path.exists(dstdir):  ##如果目录不存在，创建目录
            os.makedirs(dstdir)

        dstfn = dstdir + fn  ##生成目录下的文件名
        shutil.move(srcfn, dstfn)  ##移动

def clear(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            for f in os.listdir(path_file):
                path_file2 = os.path.join(path_file, f)
                if os.path.isfile(path_file2):
                    os.remove(path_file2)

def removeSufFix(path,len):
    filelist = os.listdir(path)  # 打印所有文件夹下的内容，可以不要这3行代码
    # for file in filelist:
    # print(file)
    for file in filelist:  # 遍历所有文件
        Olddir = os.path.join(path, file)  # 原来的文件路径
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue
        filename = os.path.splitext(file)[0]  # 分离文件名与扩展名;得到文件名
        # print(filename)
        filetype = os.path.splitext(file)[1]  # 文件扩展名
        # print(filetype)
        _len = -len
        Newdir = os.path.join(path, filename[:_len] + filetype)  # filename[:-3]是原文件去掉倒数3位
        # print(Newdir)
        os.rename(Olddir, Newdir)  # 重命名，替换原图片