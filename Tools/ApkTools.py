# coding:utf-8
import CmdTools
import ZipFileTools
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
            # os.execl(sys.executable,sys.executable)
            ZipFileTools.zip_archive(_unzip_temp_,_apk_name_)
            os.system("jarsigner -verbose -keystore {0} -signedjar {1} {2} {3} -storepass {4}".format(self._keystore,_apk_name_,_apk_name_,self._alias,self._alias_pwd))
            print "打包成功:"+_apk_name_
            v.Revert(_unzip_temp_)
        if os.path.exists(_unzip_temp_):
            print "开始删除解压文件:"+_unzip_temp_
            rmtree(_unzip_temp_)

""" configs = [
    {
        "name":"100",
        "config":[
            [CBuildCMD_FileFromString,"assets/Version/tracker.info","100"],
            [CBuildCMD_FolderRemove,"META-INF"]
        ]
    },
    {
        "name":"666",
        "config":[
            [CBuildCMD_FileFromString,"assets/Version/tracker.info","666"],
            [CBuildCMD_FolderRemove,"META-INF"]
        ]
    },
    {
        "name":"777",
        "config":[
            [CBuildCMD_FileFromString,"assets/Version/tracker.info","777"],
            [CBuildCMD_FolderRemove,"META-INF"]
        ]
    },
    {
        "name":"998",
        "config":[
            [CBuildCMD_FileFromString,"assets/Version/tracker.info","998"],
            [CBuildCMD_FolderRemove,"META-INF"]
        ]
    },
    {
        "name":"702",
        "config":[
            [CBuildCMD_FileFromString,"assets/Version/tracker.info","702"],
            [CBuildCMD_FolderRemove,"META-INF"]
        ]
    },
]

build = CBuildApk("D:/BCM.apk","D:/BCM/program/UnityProjects/GameTemplate/keystores/user.keystore","","basketball_alpha1","dj-game")
build.Config(*configs)
build.Build() """
