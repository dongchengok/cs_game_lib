#coding=utf-8
 
import os,os.path
import zipfile
from shutil import rmtree
 
def zip_archive(folder,zip_out):
    if os.access(zip_out,os.R_OK):
        print "删除已存在的"+zip_out
        os.remove(zip_out)
    print "打包中"+zip_out
    filelist = []
    if os.path.isfile(folder):
        filelist.append(folder)
    else :
        for root, dirs, files in os.walk(folder):
            for name in files:
                filelist.append(os.path.join(root, name))
        
    zf = zipfile.ZipFile(zip_out, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(folder):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()
    print "打包成功"+zip_out

def unzip_archive(filename, out_folder):
    if os.path.exists(out_folder):
        rmtree(out_folder)
        print "删除已存在的文件夹"+out_folder
    print "开始解压文件"+filename+"->"+out_folder
    with zipfile.ZipFile(filename,mode="r",allowZip64=True) as file:
        file.extractall(out_folder)
        print "解压文件成功"+filename+"->"+out_folder

