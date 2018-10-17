# coding:utf-8
import sys

class CStdoutCodecs:
    def __init__(self,file,decoding="utf-8",encoding="gbk"):
        self.__file__ = file
        self.__encoding = encoding
        self.__decoding = decoding
    def write(self,s):
        self.__file__.write(s.decode(self.__decoding).encode(self.__encoding))

def StdoutWithCodecs(decoding="utf-8",encoding="gbk"):
    sys.stdout = CStdoutCodecs(sys.stdout,decoding,encoding)
def StderrWithCodecs(decoding="utf-8",encoding="gbk"):
    sys.stderr = CStdoutCodecs(sys.stderr,decoding,encoding)