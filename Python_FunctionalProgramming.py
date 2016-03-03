#以下来自廖雪峰的Python学习之Python函数式编程

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
print('按名字排序:', sorted(L, key=by_name))    #sorted(L)本身就能排序，key就是按照某种规则排序，这里by_name这个函数就是定义按照名字的字母顺序，因为by_name就是返回名字的小写形式
#用sorted()对上述列表分别按分数排序：
def by_score(t):
	return t[1]
print('按分数排序:', sorted(L, key=by_score))
print('-----------------------------------------\n')


#返回函数//////////////////////////////////
