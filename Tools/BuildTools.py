# coding:utf-8
import os
import os.path
import sys
from shutil import rmtree,copytree
from contextlib import closing

#配置单元使用方式
#test = CBuildApkConfig.ConfigUnit("d:/haha.txt","{0}asdfasdf{1}",1,2)
#test.Config()
#test.Revert()
class CBuildCMD:
    def Config(self,root_path):
        pass
    def Revert(self,root_path):
        pass

class CBuildCMD_File(CBuildCMD):
    def __init__(self,filename):
        self._filename = filename
    def Revert(self,root_path):
        _path = os.path.join(root_path,self._filename)
        if os.access(_path,os.R_OK):
            print("删除文件:{0}".format(_path))
            os.remove(_path)

class CBuildCMD_FileFromString(CBuildCMD_File):
    def __init__(self,filename,str,*args):
        CBuildCMD_File.__init__(self,filename)
        self._str = str.format(*args)
    def Config(self,rool_path):
        _path = os.path.join(rool_path,self._filename)
        print("创建文件:{0}".format(_path))
        with closing(open(_path,"wb")) as file:
            file.write(self._str)
            file.close()
        
class CBuildCMD_FileFromFile(CBuildCMD_File):
    def __init__(self,filename,filename_src,*args):
        CBuildCMD_File.__init__(self,filename)
        self._filename_src = filename_src
        self._args = args
    def Config(self,root_path):
        str_src = None
        _path_src = os.path.join(os.getcwd(),self._filename_src)
        _path = os.path.join(root_path,self._filename)
        print("拷贝文件:{0}->{1}".format(_path_src,_path))
        with closing(open(_path_src,"rb")) as file:
            file.seek(0,2)
            count = file.tell()
            file.seek(0,0)
            str_src = file.read(count)
        if self._args!=None and len(self._args)>0:
            str_src = str_src.format(*self._args)
        with closing(open(_path,"wb")) as file:
            file.write(str_src)

class CBuildCMD_Folder:
    def __init__(self,folder,folder_src):
        self._folder = folder
        self._folder_src = folder_src
    def Config(self,root_path):
        self.Revert(root_path)
        _path_src = os.path.join(os.getcwd(),self._folder_src)
        _path = os.path.join(root_path,self._folder)
        print("拷贝文件夹:{0}->{1}".format(_path_src,_path))
        copytree(_path_src,_path)
    def Revert(self,root_path):
        _path = os.path.join(root_path,self._folder)
        print("删除文件夹:{0}".format(_path))
        if os.path.exists(_path):
            rmtree(_path)

#apk打包的配置文件
class CBuildConfig:
    def __init__(self,name):
        self.name = name
        self._configs = []

    def Setup(self,datas):
        self._configs = []
        for v in datas:
            self._configs.append(v[0](*v[1:]))
        pass

    def Config(self,root_path):
        print "正在配置:"+self.name
        for v in self._configs:
            v.Config(root_path)

    def Revert(self,root_path):
        print "正在回滚配置修改:"+self.name
        for v in self._configs:
            v.Revert(root_path)