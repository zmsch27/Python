#以下来自廖雪峰的Python学习之Python面向对象编程

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
#但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了
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
