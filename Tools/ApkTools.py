# coding:utf-8
import CmdTools
import ZipFileTools
import os
import os.path
from shutil import rmtree,copytree
from BuildTools import *

CmdTools.StdoutWithCodecs()
CmdTools.StderrWithCodecs()
    
#apk打包类
#使用方式
#apk = CBuildApk("d:/111.apk")
#apk.AddConfig("哈哈哈")
#apk.Build()
class CBuildApk:
    def __init__(self,filename,keystore,keystore_pwd,alias,alias_pwd):
        self._filename = filename
        self._keystore = keystore
        self._keystore_pwd = keystore_pwd
        self._alias = alias
        self._alias_pwd = alias_pwd
        self._config = []

    def __del__(self):
        pass
    
    def Config(self,*configs):
        self._config = []
        for v in configs:
            if type(v)==dict:
                config = CBuildConfig(v["name"])
                config.Setup(v["config"])
                self._config.append(config)
                print "添加配置:"+config.name
            elif isinstance(v,CBuildConfig):
                self._config.append(v)
    
    def Build(self):
        if self._filename.find(".apk",-4)==-1 and self._filename.find(".APK",-4)==-1:
            raise Exception("不支持非apk格式的文件:"+self._filename) 
        print "开始批量生成apk"
        _unzip_temp_ = self._filename[:-4]+"_unzip_temp_"
        ZipFileTools.unzip_archive(self._filename,_unzip_temp_)
        for v in self._config:
            _apk_name_ = self._filename[:-4]+"_"+v.name+".apk"
            print "开始打包:"+_apk_name_
            v.Config(_unzip_temp_)
            #os.execl(sys.executable,sys.executable)
            #os.system("jarsigner -verbose -keystore %keystoreFrom% -signedjar %root%\%proName%\mobile\!fileName!_tracker!tracker[%%j]!.apk pre_!fileName!_tracker!tracker[%%j]!.apk basketball_alpha1 -storepass dj-game")
            ZipFileTools.zip_archive(_unzip_temp_,_apk_name_)
            print "打包成功:"+_apk_name_
            v.Revert(_unzip_temp_)

configs = [
    {
        "name":"hohoho",
        "config":[
            [CBuildCMD_FileFromString,"haha.txt","hello world"],
            [CBuildCMD_FileFromFile,"haha.txt","D:/haha.txt","dc","cd"]
        ]
    },
    {
        "name":"hahaha",
        "config":[
            [CBuildCMD_FileFromString,"haha.txt","hello world"],
            [CBuildCMD_FileFromFile,"haha.txt","D:/haha.txt","dc","cd"]
        ]
    },
]

build = CBuildApk("D:/111.apk",1,1,1,1)
build.Config(*configs)

""" build_config = CBuildApkConfig("hello")
build_config.Init(
    [
        [CBuildCMD_FileFromString,"haha.txt","hello world"],
        [CBuildCMD_FileFromFile,"haha.txt","D:/haha.txt","dc","cd"]
    ]
) """

""" print(type(build_config)==CBuildApkConfig)
print(isinstance(build_config,CBuildApkConfig)) """

#print(type("haha")==str)