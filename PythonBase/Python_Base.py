#以下来自廖雪峰的Python学习之Python基础

name = input('输入名字：')
print('hello,',name)
print('66对应的字符：',chr(66))
print('字符a对应的数字：',ord('a'))
print('汉字\'中文\'对应的utf-8编码：','中文'.encode('utf-8'))  #转码为指定的bytes
print('字符串\'zhongwen\'对应的ASCILL编码：','zhongwen'.encode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  #解码
print(b'zhongwen'.decode('ascii'))
print('字符串\'中文\'长度：',len('中文'))  #字符串长度
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  #字节长度
print('-----------------------------------------\n')

#格式化
print('hello, %s' % name)
print('hi, %s, you have $%d' % (name, 1000))
#练习
s1 = 72
s2 = 85
r = (s2 - s1) / s1
print('提高 %.1f%%' % (r*100))
print('-----------------------------------------\n')

#list
lists = ['a', 123, True, 'b']
print(lists)
print('list长度：',len(lists))
print('得到指定的索引：lists[1]=',lists[1])   #print(lists[4]) 超出索引，报错
print('得到指定的索引:lists[-3]=',lists[-3])
lists[1] = 456
print('替换第二个值后：',lists)
lists.append('add')
print('增加一个值后：',lists)
lists.pop()
print('取出最后一个值后：',lists)
lists.pop(3)
print('取出确定的一个值后：',lists)
lists.insert(3, 'bb')
print('在一个确定的位置加入值后：',lists)
#可以是多维list
p = ['p1', 333]
lists.insert(2, p)
print('多维list：',lists)
print('拿到333：', p[1], lists[2][1])

#tuple  tuple和list非常类似，但是tuple一旦初始化就不能修改
print('\n')
tuples = (1, 'das', True, 'ere')
print(tuples)
tuples0 = ()  #0个元素
print(tuples0)
tuples1 = (1,)  #1个元素，必须这样定义，因为（）
print(tuples1)
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
print('-----------------------------------------\n')


#条件判断
age = 3
if age >= 18:
	print('age is', age, 'adult')
elif age >= 6:
    print('age is', age, 'teenager')
else :
    print('age is', age, 'kid')

birth = input('input birth: ')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')
#练习 
height = 1.70
weight = 70
bmi = weight // (height*height)
if bmi < 18.5:
	print('过轻')
elif bmi>=18.5 and bmi<25:
    print('正常')
elif bmi>=25 and bmi<28:
	print('过重')
elif bmi>=28 and bmi<32:
	print('肥胖')
else :
	print('严重肥胖')
print('-----------------------------------------\n')


#循环
#for-in循环
names = ['Michael', 'Bob', 'Tracy']
for x in names:
	print('hello,', x)

sum = 0
for x in range(10):
	sum = sum + x
print('sum = ', sum)

#while循环
sum = 0
n = 100
while n > 0:
	sum = sum + n
	n= n - 2
print('sum = ', sum)
print('-----------------------------------------\n')


#dict
dicts = {'a':12, 'b':33, 'c':77}
print(dicts)
print('dicts[\'a\'] =', dicts['a'])
print('in:', 'a' in dicts)
print('get:', dicts.get('c'))
print('pop', dicts.pop('c'))
print(dicts)

#set   set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
sets = set(['q', 123, 'rt'])
print(sets)
sets = set([1, 1, 2, 2, 3, 3])
print('set 重复没有用：', sets)
s = set([1, 2, 3])
s.add(4)
print('add:', s)
s.add(4)
print(s)
s.remove(4)
print('remove:', s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('s1 & s2:', s1 & s2)
print('s1 | s2:', s1 | s2)

#不可变对象
#a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'
a = ['c', 'b', 'a']
a.sort()
print('sort:', a)

#当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
#相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了
#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的
a = 'abc'
print(a.replace('a', 'A'))
print('replace:', a)

a = 'abc'
b = a.replace('a', 'A')
print('replace:', b)
print('replace:', a)