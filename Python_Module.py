#以下来自廖雪峰的Python学习之Python模块

#在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。
#为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
#在Python中，一个.py文件就称之为一个模块（Module）。
#为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
#请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
#__init__.py可以是空文件，也可以有Python代码

#使用模块//////////////////////////////////
#!user/nin/env python3
'a test module'
__author__ = 'zmsch27'

import sys
def test():
	args = sys.argv
	if len(args)==1:
		print('Hello World')
	elif len(args)==2:
		print('Hello %s!' % args[1])
	else:
		print('To many arguments!')

if __name__=='__main__':
	test()
print('-----------------------------------------')

#作用域------------------------------------------
#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
#private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量。
#但是，从编程习惯上不应该引用private函数或变量。
def _private_1(name):
	return 'Hi, %s' % name
def _private_2(name):
	return 'Hello, %s' % name
def greating(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)
#在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
print('-----------------------------------------\n')