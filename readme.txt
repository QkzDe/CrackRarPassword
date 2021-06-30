一、字典生成两种方式：
  1.生成字典到txt里，用脚本一行行读取密码进行试验，缺点就是如果字典过大可能导致内存打不开文件

  2.代码遍历拼接出密码试验

因此代码有两种方式，读取字典、循环拼接密码
python主要依赖rarfile包，其中extractall为核心函数

如果想要破解zip压缩文件，可改为导入zirfile包并将rarfile.RarFile(rar_name)改为zipfile.ZipFile()

二、帮助工具：

文件夹里有zip的暴力破解工具ARPR，傻瓜式使用，但只能用于zip和低版本的rar，打开rar时会报错：选择的不是rar文件

文件夹里还有字典生成器superdic，一键生成到txt里

注意：需要配置winrar.exe的环境变量rarfile包才能正常使用，报错 rarfile.RarCannotExec: Cannot find working tool.
解决方法：https://blog.csdn.net/im_hwp/article/details/108724749
