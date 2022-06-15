#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FilePath: /PyWebView/vue-pywebview-pyinstaller/pyapp/api/api.py
Author: 潘高
LastEditors: 潘高
Date: 2022-03-21 17:01:39
LastEditTime: 2022-03-23 15:40:25
Description: 本地API，供前端JS调用
usage: 调用window.pywebview.api.<methodname>(<parameters>)从Javascript执行
'''

import getpass
import os
import webview
from decimal import Decimal
# from pdf_utils import gen_pdf_outlines
from PyPDF2 import PdfFileReader as pdf_read


#每个书签的索引格式
#{'/Title': '书签名', '/Page': '指向的目标页数', '/Type': '类型'}

directory_str = ''

def bookmark_listhandler(list):
    global directory_str
    for message in list:
        if isinstance(message, dict):
            directory_str += "# " + message['/Title'] + '\n\n'
        else:
            bookmark_listhandler(message)

def gen_pdf_outlines(pdf_path):
    # pdf_path = "D:\\dl-nut\\我的坚果云\\XXX-B·卡尔-201108.pdf"
    with open(pdf_path, 'rb') as f:
        pdf = pdf_read(f)
        #检索文档中存在的文本大纲,返回的对象是一个嵌套的列表
        text_outline_list = pdf.getOutlines()
        bookmark_listhandler(text_outline_list)

    with open(pdf_path + '.txt', 'w', encoding='utf-8') as f:
        f.write(directory_str)

    return pdf_path + '.txt'


class API:
    
    def getOwner(self):
        return getpass.getuser()

    def getSum(self, a, b):
        # print(str(a), str(b))
        return str(Decimal(str(a)) + Decimal(str(b)))
        
    def execCode(self, str): 
        exec(str)
        return '代码执行成功'
 
    def makeDir(self, dir):
        os.makedirs(dir)
        return dir

    def openFiles(self):
        # file_types = ('Image Files (*.bmp;*.jpg;*.gif)', 'All files (*.*)')
        result = self.window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True)
        return result

    def openPdfFile(self):
        file_types = ('Pdf files (*.pdf)', 'All files (*.*)')
        result = self.window.create_file_dialog(webview.OPEN_DIALOG, file_types=file_types)
        return result

    def openFolder(self):
        result = self.window.create_file_dialog(webview.FOLDER_DIALOG)
        return result

    def genPdfOutlines(self, pdfPath):
        return gen_pdf_outlines(pdfPath)




