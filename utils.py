import os
import datetime

PATH_SRC = 'src'
PATH_NOTE = 'notes'
LATEX_FILE = ['00.main.tex', 'def.tex']
FILE_NAME = '__init__.py'

def create_folder(name, dest=''):
    try:
        path = os.path.join(dest, name)
        os.makedirs(path)
    except Exception as ex:
        print("Error when create folder: {}".format(str(ex)))

def init_latex_folder(dest):
    try:
        create_latex_file(LATEX_FILE[0], dest)
        create_latex_file(LATEX_FILE[1], dest, 'Custom define')
    except Exception as ex:
        print("Error when init Latex folder: {}".format(str(ex)))

def create_latex_file(name, dest='', additional_content=''):
    try:
        # Check file extension is .tex
        filename, extension = os.path.splitext(name)
        if extension != '.tex':
            name = ''.join([name, '.tex'])

        # Check if file is exited
        file_path = os.path.join(dest, name)
        if os.path.isfile(file_path):
            print("File {} is existed".format(file_path))
            exit

        # Create file and add created date in comment
        init_string = ''.join(['%%----- Create date: ', datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S'), ' -----\n'])
        with open(file_path, 'w+') as file:
            file.write(init_string)
            if additional_content:
                file.write(''.join(['%%----- ', additional_content.strip(), ' -----\n']))

    except Exception as ex:
        print("Error when create Latex file: {}".format(str(ex)))

def create_init_py(dest=''):
    HEAD_INFO = '''\'''
Date created: {}
Author: Nguyen Dang Tran Ngoc
\'''
'''.format(datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S'))
    
    try:
        file_path = os.path.join(dest, FILE_NAME)
        with open(file_path, 'w+') as file:
            file.writelines(HEAD_INFO)

    except Exception as ex:
        print("Error when create init file: {}".format(str(ex)))

# for i in range(1, 29):
#     name = ''.join(['chapter_',"{:02d}".format(i)])
#     print("Create folfder: {}".format(name))
#     create_folder(name, PATH_NOTE)
#     init_latex_folder(os.path.join(PATH_NOTE, name))

create_init_py('data')
