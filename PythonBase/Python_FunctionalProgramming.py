#以下来自廖雪峰的Python学习之Python函数式编程

import functools
#我们首先要搞明白计算机（Computer）和计算（Compute）的概念。
#在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。
#而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。
#对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

#高阶函数///////////////////////////////////
#变量可以指向函数
print('abs(-10) =', abs(-10))
print('abs =', abs)
f = abs
print('f =', f)
print('f(-10) =', f(-10))
#函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数!如果把abs指向其他对象，会有什么情况发生？
#abs = 10
#print('abs(-10) =', abs(-10))     #这个会报错

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, z):
	return z(x) + z(y)
result = add(-9, 2, abs)
print('add(-9, 2, abs) =', result)
#编写高阶函数，就是让函数的参数能够接收别的函数。       把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
print('-----------------------------------------')

#map/reduce----------------
#我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
L = list(range(1, 11))
def f(x):
	return x*x
r = map(f, L)
print('map：', list(r))
#把list里所有的数字改为字符串
L = list(range(1, 11))
r = list(map(str, L))
print('map：', r)
#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
L = list(range(1, 11))
def add(x, y):
	return x+y
r = reduce(add, L)
print('reduce：', r)
#把str转换为int的函数：
def strtoint(s):
	def fn(x, y):
		return x*10+y
	def chartonum(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, list(map(chartonum, s)))
print('strtoint:', strtoint('13579'))
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
L = ['adam', 'LISA', 'barT']
def normalize(name):
	return name.title()
print('练习:', list(map(normalize, L)))
print('-----------------------------------------')

#filter---------------------
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#在一个list中，删掉偶数，只保留奇数
from collections import Iterator
L = [1, 2, 4, 5, 6, 9, 10, 15]
def is_odd(x):
	return x % 2 == 1
r = filter(is_odd, L)
print('isIterator:', isinstance(r, Iterator))
print('奇数:', list(r))
#把一个序列中的空字符串删掉，可以这么写：
L = ['A', '', 'B', None, 'C', '  ']
def is_empty(s):
	return s and s.strip()
r = filter(is_empty, L)
print('去除空字符串:', list(r))
print('None:', None)
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。利用filter()滤掉非回数
#原来的问题 ：
#if s[i] == s[len(s)-1-i]:
#            return True
#是因为一个数所有i里 只要有一个i满足条件就会被return出来，1000以内的数只要头尾相同就是回文数 所以return出来 没看出问题，1000以上就出问题了
#如1021，头尾相同（有个i满足条件），1021就被return出来了，然而1021不是回文数。
#改成：
# if s[i] != s[len(s) - 1 - i]:
#            return False
# 一个数 只要有一个i不满足条件 就不能被filter滤出。所以出来的一定就是回文数
def is_palindrome(n):
	s = str(n)
	for i in range(len(s)):
		if s[i] != s[len(s)-1-i]:
			return False
		else:
			pass    #如果直接返回true，如1021直接就返回了
	return True
result = filter(is_palindrome, range(1, 10002))
print('回数:', list(result))
print('-----------------------------------------')

#sorted-----------------
#Python内置的sorted()函数就可以对list进行排序
L = [36, 5, -12, 9, -21]
print('数字排序:', sorted(L))
#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
#然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素
print('数字绝对值排序:', sorted(L, key=abs))
#字符串排排序
L = ['bob', 'about', 'Zoo', 'Credit']
#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print('字符串排序:', sorted(L))
#忽略大小写,按照字母序排序排序
print('按字母顺序:', sorted(L, key=str.lower))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print('按字母逆序:', sorted(L, key=str.lower, reverse=True))
#假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#用sorted()对上述列表分别按名字排序：
def by_name(t):
	return t[0].lower()   #解释一下：这里的t就是L的每一个元素
#sorted(L)本身就能排序，key就是按照某种规则排序，这里by_name这个函数就是定义按照名字的字母顺序，因为by_name就是返回名字的小写形式
print('按名字排序:', sorted(L, key=by_name))
#用sorted()对上述列表分别按分数排序：
def by_score(t):
	return t[1]
print('按分数排序:', sorted(L, key=by_score))
print('-----------------------------------------\n')


#返回函数//////////////////////////////////
#函数作为返回值----------------------
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
	ax = 0
	for x in args:
		ax = ax + x
	return ax
#但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
	def sum():
		ax = 0
		for x in args:
			ax = ax + x
		return ax
	return sum
#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1, 3, 5, 7, 9)
print('f:', f)
print('f():', f())
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print('f1 == f2:', f1 == f2)

#闭包
#注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
#另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子:
def count():
	fs = []
	for x in range(1, 4):
		def f():
			return x*x
		fs.append(f)
	return fs
f1, f2, f3 = count()
#在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。   你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
print('f1() =', f1())
print('f2() =', f2())
print('f3() =', f3())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
#这里看不很懂---------------------------------------------------
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print('f1() =', f1())
print('f2() =', f2())
print('f3() =', f3())
#一个函数可以返回一个计算结果，也可以返回一个函数。
#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
print('-----------------------------------------\n')


#匿名函数/////////////////////////////////////
#Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
#在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
xx = map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print('list(xx) =', list(xx))
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x*x
print('f =', f)
print('f(5) =', f(5))
#同样，也可以把匿名函数作为返回值返回:
def build(x, y):
	return lambda: x*x + x*y
print('build(3, 4) =', build(3, 4)())  #这里加个()因为返回的是个匿名函数
print('-----------------------------------------\n')


#装饰器/////////////////////////////////////其实装饰器就是拦截器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print('2015-3-25')
f = now
f()
#函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
#现在，假设我们要增强now()函数的功能
#比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
print('-----------------------------------------\n')


#偏函数/////////////////////////////////////////
#在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：
#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print('int(\'12345\') =', int('12345'))
#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print('int(\'12345\', base=16) =', int('12345', base=16))
print('int(\'12345\', base=8) =', int('12345', base=8))
#假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
	return int(x, base)
print('int2(\'1000000\') =', int2('1000000'))
print('int2(\'1010101\') =', int2('1010101'))
#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
int2 = functools.partial(int, base=2)
print('int2(\'1000000\') =', int2('1000000'))
print('int2(\'1010101\') =', int2('1010101'))
#所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值
print('int2(\'1000000\', base=10) =', int2('1000000', base=10))
#最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：int2 = functools.partial(int, base=2)实际上固定了int()函数的关键字参数base，
#也就是：int2('10010')相当于：
kw = { 'base': 2 }
int('10010', **kw)
#当传入：max2 = functools.partial(max, 10)实际上会把10作为*args的一部分自动加到左边，也就是：max2(5, 6, 7)相当于：args = (10, 5, 6, 7)  max(*args)结果为10。