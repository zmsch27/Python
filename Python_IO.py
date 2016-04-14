#以下来自廖雪峰的Python学习之PythonIO编程

import os
#IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。
#Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。
#对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。
#由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。
#第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；
#另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称为异步IO。

#文件读写/////////////////////////////////////////
try:
	f = open('D:/io.txt', 'r')
	print(f.read())
finally:
	if f:
		f.close()

#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('D:/io.txt', 'r') as f:
	print(f.read())
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
#另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
with open('D:/io.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
print('-----------------------------------------')

#二进制文件---------------------------------------------
#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open('D:/教父.jpg', 'rb')
print(f.read())
print('-----------------------------------------')

#字符编码--------------------------------------------------
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f.read()
#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
#遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
print('-----------------------------------------')

#写文件----------------------------------------------
#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('D:/io.txt', 'w') as f:
	f.write('hello')
f = open('D:/io.txt', 'r')
print(f.read())
#要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
print('-----------------------------------------\n')


#StringIO和BytesIO//////////////////////////////////////////////
#StringIO-------------------------------------------------------
#很多时候，数据读写不一定是文件，也可以在内存中读写。
#StringIO顾名思义就是在内存中读写str。
#要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
    if s=='':
    	break
    else:
    	print(s.strip())
print('-----------------------------------------')

#BytesIO---------------------------------
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
from io import BytesIO
f = BytesIO()
f.write('谢谢'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
#StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
print('-----------------------------------------\n')


#操作文件和目录////////////////////////////////////
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
print(os.path.abspath('.'))
os.path.join('D:/Python', 'test')
os.mkdir('D:/Python/test')
os.rmdir('D:/Python/test')
#要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
os.path.split('/Users/michael/testdir/file.txt')
#os.path.splitext()可以直接让你得到文件扩展名
os.path.splitext('/Users/michael/testdir/file.txt')
#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
#利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print(x for x in os.listdir('.') if os.path.isdir(x))
#要列出所有的.py文件，也只需一行代码：
print(x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py')
print('-----------------------------------------\n')


#序列化////////////////////////////////////////////
#在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
d = dict(name='Bob', age=20, score=88)
#可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。
#如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。
#我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
#Python提供了pickle模块来实现序列化。
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
#或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
#也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print('-----------------------------------------')

#JSON------------------------------------------------------
#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
#要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
print('-----------------------------------------')

#JSON进阶-----------------------------------------------
#Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
#这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print(json.dumps(s, default=student2dict))
#同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象
#然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))