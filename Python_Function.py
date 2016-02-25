#以下来自廖雪峰的Python学习之Python函数

import math #语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数

#Python自带函数////////////////////////////////////////////////
print('abs(-1) =', abs(-1))
print('abs(88) =', abs(88))
#max()可以接收任意多个参数，并返回最大的那个
print('max(1, 2, 3, 78, 54, 22, 77) =', max(1, 2, 3, 78, 54, 22, 77))
#数据类型转换函数
print('int(\'123\') =', int('123'))
print('int(12.34) =', int(12.34))
print('float(\'12.34\') =', float('12.34'))
print('str(1.23) =', str(1.23))
print('str(100) =', str(100))
print('bool(1) =', bool(1))
print('bool(0) =', bool(0))
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print('a(-3) =', a(-3))
print('-----------------------------------------\n')

#自定义函数/////////////////////////////////////////////////////
#空函数--------------
def nop():
	#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
    #pass还可以用在其他语句里，比如：
    #if age >= 18:
        #pass
    #缺少了pass，代码运行就会有语法错误
	pass

#自定义abs函数-----------
def my_abs(x):
	if not isinstance(x, (float, int)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print('自定义函数my_abs(-10) =', my_abs(-10))

#返回多个值------------
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print('x ,y =', x, y)
#但其实这只是一种假象，Python函数返回的仍然是单一值
result = move(100, 100, 60, math.pi / 6)
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple,按位置赋给对应的值
#所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
print('result =', result)
print('-----------------------------------------\n')

#函数参数///////////////////////////////////////////
#位置参数----------
def powser(x):
	return x*x
#对于power(x)函数，参数x就是一个位置参数。当我们调用power函数时，必须传入有且仅有的一个参数x
print('powser(5) =', powser(5))


#默认参数----------------------
def powser1(x, n=2):
	sum = 1;
	while n>0:
		n = n - 1
		sum = sum * x
	return sum
#这样，当我们调用power(5)时，相当于调用power(5, 2)
print('powser1(5) =', powser1(5))
print('powser1(5, 3) =', powser1(5, 3))

def enroll(name, gender, age=6, city='BeiJing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
#大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数
print('-----------------------------------------')
enroll('Sarah', 'F')
#只有与默认参数不符的学生才需要提供额外的信息
print('-----------------------------------------')
enroll('Bob', 'M', 7)
#可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
#比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值
print('-----------------------------------------')
enroll('Adam', 'M', city='Tianjin')
print('-----------------------------------------')
#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑
def add_end(L=[]):
	L.append('END')
	return L
#当你正常调用时，结果似乎不错：
print('add_end:', add_end([1, 2, 3]))
print('add_end:', add_end(['x', 'y', 'z']))
#连续2次使用默认参数调用add_end()时，结果就不对了
print('add_end默认参数：', add_end())
print('add_end默认参数：', add_end())
#原因解释如下：
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
#每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现:
print('-----------------------------------------')
def add_end_None(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
print('add_end_None默认参数：', add_end_None())
print('add_end_None默认参数：', add_end_None())
#PS:为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
#此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

#可变参数-----------------
