# 用于生成目录md文件
import os


PDF_PATH = 'web/pdf/'
FILE_NAME = 'README.md'
url = 'http://asahimoon.gitee.io/pdfviwer/web/viwer.html?file=pdf/'

pdf_index = os.listdir(PDF_PATH)

# 覆盖写入目录
with open(FILE_NAME, 'w', encoding='UTF-8') as f:
    f.write('# 目录 \n')

    for index in pdf_index:
        f.write('## '+index+'\n')

        front = PDF_PATH + index + '/'
        books = os.listdir(front)
        for book in books:
            link = url + index + '/' + book 
            link = link.replace(' ','%20')
            f.write('+ ['+book+']('+link+')\n') 
