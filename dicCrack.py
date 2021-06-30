import optparse
import zipfile
from threading import Thread
from tqdm import tqdm
import rarfile


def extract_file(rar_file, password):
    """ 提取压缩文件，通过密码不断尝试 """
    try:
        rar_file.extractall(pwd=bytes(password, 'utf-8'))
        print(f'\n  发现密码，正确密码为：{password}')
        return True
    except:
        pass
        return  False


def main():
    # """ 通过optparse模块进行py命令行形式脚本操作，获取字典和zip路径 """
    # parser = optparse.OptionParser('\n  %prog -z <zipfile> -d <dictionary>')
    # parser.add_option('-z', dest='zname', type='string', help='specify zip file')
    # parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    # options, args = parser.parse_args()
    # if options.zname and options.dname:
    #     zip_name = options.zname
    #     dict_name = options.dname
    # else:
    #     print(parser.usage)
    #     exit(0)


    #测试用的目录文件,为了用pycharm调试，可将上述代码注释掉
    #字典路径和文件路径
    rar_name = 'F:/JetBrains/PycharmProjects/rarattack/password.rar'
    dict_name = 'C:/Users/QKZ/Desktop/password.txt'

    #进度条库:tqdm
    try:
        rar_file = rarfile.RarFile(rar_name)
        with open(dict_name, 'r', encoding='utf-8') as f:
            for line in tqdm(f.readlines()):
                password = line.strip('\n')
                if extract_file(rar_file, password) :
                   rar_file.close()
                   break

    except Exception as e:
        print(f'发生异常！请检查文件是否存在！异常信息为：{e}')


main()