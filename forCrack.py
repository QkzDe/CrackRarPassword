import itertools
import string
import rarfile
import sys

path = "F:\\JetBrains\\PycharmProjects\\rarattack\\password.rar"                #文件路径
myrar = rarfile.RarFile(path)
i=4
#chars=string.digits+string.ascii_letters    #密码组成：数字+字母（包括大小写）
chars=string.digits
def bruteforce(myrar,password):
    """强行破解密码"""
    try:
        myrar.extractall(pwd=password.encode())
        return True

    except Exception as e:
        print('尝试密码错误：',password)
        return False

while i<=4:         #密码位数，不大于4位
    passwords=itertools.product(chars,repeat=i)
    for item in passwords:
        pwd=''.join(item)
        if bruteforce(myrar,pwd):
            print("正确密码是："+pwd)
            myrar.close()
            sys.exit()          #退出程序
    i+=1
