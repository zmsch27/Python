#以下来自廖雪峰的Python学习之Python常用内建模块

#datetime////////////////////////////////////////
#datetime是Python处理日期和时间的标准库。

#获取当前日期和时间--------------------------------
from datetime import datetime
now = datetime.now()
print(now)
#注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
#如果仅导入import datetime，则必须引用全名datetime.datetime。
#datetime.now()返回当前日期和时间，其类型是datetime。
print('-----------------------------------------')

#获取指定日期和时间----------------------------------
#要指定某个日期和时间，我们直接用参数构造一个datetime：
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
print('-----------------------------------------')

#datetime转换为timestamp--------------------------------------
dt = datetime(2015, 4, 19, 12, 20)
dt.timestamp()
print(dt)
#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
#某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
print('-----------------------------------------')

#timestamp转换为datetime------------------------------------------
#要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
t = 1429417200.0
print(datetime.fromtimestamp(t))  #本地时间
#timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(t))
print('-----------------------------------------')

#str转换为datetime---------------------------------------------
#很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
#字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。  注意转换后的datetime是没有时区信息的。
print('-----------------------------------------')

#datetime转换为str-----------------------------------------
#如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print('-----------------------------------------')

#datetime加减-------------------------------------------
#对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类
from datetime import datetime, timedelta
now = datetime.now()
print(now + timedelta(hours=10))
print(now + timedelta(days=1))
print(now + timedelta(days=2, hours=12))
print('-----------------------------------------\n')


#collections///////////////////////////////////////////
#collections是Python内建的一个集合模块，提供了许多有用的集合类。

#namedtuple-----------------------------------------
#我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
p = (1, 2)
#但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
#定义一个class又小题大做了，这时，namedtuple就派上了用场：
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
#类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])
print('-----------------------------------------')

#deque-----------------------------------------
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
print('-----------------------------------------')

#defaultdict------------------------------------------
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值
#注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
#除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
print('-----------------------------------------')

#OrderedDict---------------------------------------------
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict的Key是有序的
#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：=======================
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys())) # 按照插入的Key的顺序返回
#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
print('-----------------------------------------')

#Counter--------------------------------------------------
#Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
#Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
print('-----------------------------------------\n')


#struct////////////////////////////////////////////////
#Python没有专门处理字节的数据类型。
#Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
#struct的pack函数把任意数据类型变成bytes：
import struct
print(struct.pack('>I', 10240099))
#pack的第一个参数是处理指令，'>I'的意思是：  >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

#unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
#根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
print('-----------------------------------------\n')


#hashlib///////////////////////////////////////////////////
#摘要算法简介------------------------------------
#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
#什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
print('-----------------------------------------\n')


#itertools///////////////////////////////////////////////
#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
#import itertools
#natuals = itertools.count(1)
#for i in natuals:
	#print(i)
#因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
#cycle()会把传入的一个序列无限重复下去：
#cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
#for c in cs:
    #print(c)
#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
import itertools
ns = itertools.repeat('s', 3)
for x in ns:
	print(x)

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))
print('-----------------------------------------')

#chain()--------------------------------------------------
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('abc', 'def'):
	print(c)
print('-----------------------------------------')


#groupby()-------------------------------------------------
#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
#实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
#如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
print('-----------------------------------------\n')


#XML/////////////////////////////////////////////////
#操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
#SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element:%s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
print('-----------------------------------------\n')


#urllib///////////////////////////////////////////////////
#urllib提供了一系列用于操作URL的功能。

#Get-----------------------------------------------
#urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
#例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))

#如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
#例如，模拟iPhone 6去请求豆瓣首页：
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
print('-----------------------------------------')

#Post----------------------------------------------------
#如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
#我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
from urllib import request, parse
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
print('-----------------------------------------')

#Handler---------------------------------------------------
#如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass