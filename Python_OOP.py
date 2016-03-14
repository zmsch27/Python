#以下来自廖雪峰的Python学习之Python面向对象编程

import types
#面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
#为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
#而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
#在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

#假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
#处理学生成绩可以通过函数实现，比如打印学生的成绩
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
print_score(std1)
print_score(std2)

#如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）。
#如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s : %s' % (self.name, self.score))
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
print('bart.print_score() =', bart.print_score())
print('lisa.print_score() =', lisa.print_score())
print('-----------------------------------------\n')


#类和实例////////////////////////////////////
#面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板
#比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同
class Student(object):
	pass
#class后面紧接着是类名，即Student，类名通常是大写开头的单词
#紧接着是(object)，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
#定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
bart = Student()
print('bart =', bart)
print('Student =', Student)
#可以看到，变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类
#由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
#除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
print('-----------------------------------------')

#数据封装-----------------------------------
#但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样就把“数据”给封装起来了
#这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart', 99)
print('bart.print_score() =', bart.print_score())
print('bart.get_grade() =', bart.get_grade())
print('-----------------------------------------\n')


#访问限制/////////////////////////////////////
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
#改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score
bart = Student('Bart', 89)
bart.print_score()
#这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
#但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法
#如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_name(self, name):
		self.__name = name
	def set_score(self, score):
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
bart = Student('Bart', 89)
print('bart.get_name:', bart.get_name())
print('bart.get_score:', bart.get_score())
bart.set_name('dd')
bart.set_score(999)
print('bart.get_name:', bart.get_name())
print('bart.get_score:', bart.get_score())
#需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量
#特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
#有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的
#但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
#仍然可以通过_Student__name来访问__name变量：
print('bart._Student__name =', bart._Student__name)
#总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉
print('-----------------------------------------\n')


#继承和多态////////////////////////////////////////
#在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承
#新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
class Animal(object):
	def run(self):
		print('Animal is running...')
#当我们需要编写Dog和Cat类时，就可以直接从Animal类继承
class Cat(Animal):
	pass
class Dog(Animal):
	pass
#对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
#由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法
cat = Cat()
dog = Dog()
cat.run()
dog.run()
#当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
#多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可
#由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
#对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat上
#由运行时该对象的确切类型决定，这就是多态真正的威力：
#调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的函数。
print('-----------------------------------------')

#静态语言vs动态语言---------------------------------------------------
#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
#Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。
#许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
print('-----------------------------------------\n')


#获取对象信息/////////////////////////////////////
#当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
#使用type()-----------------------------------------
#首先，我们来判断对象类型，使用type()函数：
#基本类型都可以用type()判断：
print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
#如果一个变量指向函数或者类，也可以用type()判断：
print('type(abs) =', type(abs))
a = Animal()
print('type(a) =', type(a))
#type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
print('type(123)==type(456):', type(123)==type(456))
print('type(123)==int:', type(123)==int)
print('type(\'abc\')==type(\'123\'):', type('abc')==type('123'))
print('type(\'abc\')==str:', type('abc')==str)
print('type(\'abc\')==type(123):', type('abc')==type(123))
#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
def fn():
	pass
print('type(fn)==types.FunctionType:', type(fn)==types.FunctionType)
print('type(abs)==types.BuiltinFunctionType:', type(abs)==types.BuiltinFunctionType)
print('type(lambda x: x)==types.LambdaType:', type(lambda x: x)==types.LambdaType)
print('type((x for x in range(10)))==types.GeneratorType:', type((x for x in range(10)))==types.GeneratorType)
print('-----------------------------------------')

#使用isinstance()----------------------------------------
#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
#我们回顾上次的例子，如果继承关系是：  object -> Animal -> Dog/Cat
d = Dog()
c = Cat()
a = Animal()
print('isinstance(a, Dog) =', isinstance(a, Dog))
print('isinstance(a, Animal) =', isinstance(a, Animal))
print('isinstance(c, Animal) =', isinstance(c, Animal))
#能用type()判断的基本类型也可以用isinstance()判断：
print('isinstance(123, int) =', isinstance(123, int))
print('isinstance(\'123\', str) =', isinstance('123', str))
#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print('isinstance([1, 2, 3], (list, tuple)) =', isinstance([1, 2, 3], (list, tuple)))
print('isinstance((1, 2, 3), (list, tuple)) =', isinstance((1, 2, 3), (list, tuple)))
print('-----------------------------------------')

#使用dir()------------------------------------------------
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print('dir(\'ABC\') =', dir('ABC'))
print('dir(str) =', dir(str))
#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
#紧接着，可以测试该对象的属性：
print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
print('obj.x =', obj.x)
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'
#可以传入一个default参数，如果属性不存在，就返回默认值：
print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))
#也可以获得对象的方法：
print('hasattr(obj, \'power\') =', hasattr(obj, 'power')) # 有属性'power'吗？
print('getattr(obj, \'power\') =', getattr(obj, 'power')) # 获取属性'power'
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print('fn =', fn) # fn指向obj.power
print('fn() =', fn()) # 调用fn()与调用obj.power()是一样的
print('-----------------------------------------\n')


#实例属性和类属性///////////////////////////////////////
#给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name
s = Student('Bob')
#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student(object):
    name = 'Student'
#当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
s = Student() # 创建实例s
print('s.name =', s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print('Student.name =', Student.name) # 打印类的name属性
s.name = 'Michael' # 给实例绑定name属性
print('s.name =', s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print('Student.name =', Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print('s.name =', s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
#从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字
#因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。