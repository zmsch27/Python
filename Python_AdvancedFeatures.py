#以下来自廖雪峰的Python学习之Python高级特性

#切片//////////////////////////////////////////
#取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']取前3个元素，应该怎么做？
#可以写个循环
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
n = 3
r = []
for x in range(n):
	r.append(L[x])
print('list的前三个元素：', r)
#对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。对应上面的问题，取前3个元素，用一行代码就可以完成切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print('L[0:3] =', L[0:3])
#如果第一个索引是0，还可以省略：
print('L[:3] =', L[:3])
#也可以从索引1开始，取出2个元素出来：
print('L[1:3] =', L[1:3])
#Python支持倒数切片
print('L[-2:] =', L[-2:])
#可以通过切片轻松取出某一段数列
List = list(range(100))
print('List[:10] =', List[:10])
print('List[-10:] =', List[-10:])
print('List[10:20] =', List[10:20])
#前10个数，每两个取一个
print('List[0:10:2] =', List[0:10:2])
#所有数，每5个取一个
print('List[::5] =', List[::5])
#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
Tuple = tuple(range(10))
print('Tuple[:5] =', Tuple[:5])
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
String = 'ksadjiowenfhefwe'
print('String[2:6:2] =', String[2:6:2])
<<<<<<< HEAD
=======
print('-----------------------------------------\n')


#迭代//////////////////////////////////////
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
#Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
#list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
d = {'a':1, 'b':2, 'c':3}
for key in d:
	print('key =', key)
#如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()
for value in d.values():
	print('value =', value)
for k, v in d.items():
	print('k, v =', k, v)
#由于字符串也是可迭代对象，因此，也可以作用于for循环
for ch in 'ABC':
    print('ch =', ch)
#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate('abc'):
	print(i, value)
#上面的for循环里，同时引用了两个变量，在Python里是很常见的
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
print('-----------------------------------------\n')


#列表生成式
#要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
print('list(range(1, 11)) =', list(range(1, 11)))
#生成1-10的平方,方法一是循环：
L = []
for x in list(range(1,11)):
	L.append(x * x)
print('L =', L)
#方法二是采用列表生成式：
p = [x * x for x in list(range(1, 11))]
print('1-10的平方：', p)
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来  for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
p = [x*x for x in list(range(1, 11)) if x%2 == 0]
print('1-10中偶数的平方：', p)
#还可以使用两层循环，可以生成全排列
p = [m+n for m in 'abc' for n in 'def']
print('全排列：', p)
#for循环其实可以同时使用两个甚至多个变量,例如第50行   因此，列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
p = [k+'='+v for k,v in d.items()]
print('2个变量列表生成式：', p)
#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
p = [s.lower() for s in L]
print('字符串变小写：', p)
#list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错   使用内建的isinstance函数可以判断一个变量是不是字符串
#修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print('练习：', L2)
print('-----------------------------------------\n')


#生成器：generator/////////////////////////////
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
print('L =', L)
g = (x * x for x in range(10))
print('g =', g)
#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
#每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
#正确的方法是使用for循环，因为generator也是可迭代对象   或者用列表表达式
printg = [x for x in g]
print('printg =', printg)
#我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误
#定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
	print('step1:')
	yield 1
	print('step2:')
	yield 2
	print('step3:')
	yield 3
#调用该generator时，首先要生成一个generator对象
o = odd()
print(next(o))
print(next(o))
print(next(o))
#杨辉三角    这个没看懂-------------------
def triangles():
    l = [1]
    yield l
    while True:
        l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
        yield l
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
print('-----------------------------------------\n')


#迭代器/////////////////////////////////////////////
#可以直接作用于for循环的数据类型有以下几种：一类是集合数据类型，如list、tuple、dict、set、str等；一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable    可以使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
print('isinstance([], Iterable) =', isinstance([], Iterable))
print('isinstance({}, Iterable) =', isinstance({}, Iterable))
print('isinstance(\'abc\', Iterable) =', isinstance('abc', Iterable))
print('isinstance((x for x in range(10)), Iterable) =', isinstance((x for x in range(10)), Iterable))
print('isinstance(100, Iterable) =', isinstance(100, Iterable))
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。    可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator
print('isinstance((x for x in range(10)), Iterator) =', isinstance((x for x in range(10)), Iterator))
print('isinstance([], Iterator) =', isinstance([], Iterator))
print('isinstance({}, Iterator) =', isinstance({}, Iterator))
print('isinstance(\'abc\', Iterator) =', isinstance('abc', Iterator))
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。    把list、dict、str等Iterable变成Iterator可以使用iter()函数
print('isinstance(iter([]), Iterator) =', isinstance(iter([]), Iterator))
print('isinstance(iter(\'abc\'), Iterator) =', isinstance(iter('abc'), Iterator))
#为什么list、dict、str等数据类型不是Iterator？
#这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。