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
