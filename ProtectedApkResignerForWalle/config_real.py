#!/usr/bin/python  
# -*-coding:utf-8-*-

# keystore信息
# Windows 下路径分割线请注意使用\\转义
keystorePath = "app/quysNovel.jks"
keyAlias = "quysNovel"
keystorePassword = "quys123456"
keyPassword = "quys123456"

import os

# 加固后的源文件名（未重签名）
# protectedSourceApkName = "your protected.apk"


# python3 : os.listdir()即可，这里使用兼容python2的os.listdir('.')
# 遍历出当前文件所在文件夹下的所有文件中扩展名为.apk的文件，找到后停止循环
for file in os.listdir('.'):
    if os.path.isfile(file):
        extension = os.path.splitext(file)[1][1:]
        if extension == 'apk':
            protectedSourceApkName = os.path.basename(file)
            print('===加固后未签名的源文件路径: ===', os.path.abspath(file))
            break

# 加固后的源文件所在文件夹路径(...path),注意结尾不要带分隔符，默认在此文件夹根目录
protectedSourceApkDirPath = ""
# 渠道包输出路径，默认在此文件夹Channels目录下
channelsOutputFilePath = ""
# 渠道名配置文件路径，默认在此文件夹根目录
channelFilePath = ""
# 额外信息配置文件（绝对路径，例如/Users/mac/Desktop/walle360/config.json）
# 配置信息示例参看https://github.com/Meituan-Dianping/walle/blob/master/app/config.json
extraChannelFilePath = ""
# Android SDK buidtools path , please use above 25.0+
sdkBuildToolPath = "D:\\Sdk\\build-tools\\29.0.3"
