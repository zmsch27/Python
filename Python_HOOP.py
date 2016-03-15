#以下来自廖雪峰的Python学习之Python面向对象高级编程

#数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。    多重继承、定制类、元类等概念。

#使用__slots__////////////////////////////////////////
#当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
	pass
#然后，尝试给实例绑定一个属性：
s = Student()
s.name = 'Michael'
print('s.name =', s.name)
#还可以尝试给实例绑定一个方法：
def set_age(self, age):
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print('s.age =', s.age)
#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
#s2.set_age(30)    这个有错误，因为别的实例不能调用另一个实例绑定的方法
#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, Student)
s2.set_score(40)
print('s2.set_score =', s2.score)
#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class People(object):
	__slots__ = ('name', 'age')
p = People()
p.name = 'Job'
p.age = 13
#p.score = 99    由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduatePeople(People):
    pass
g = GraduatePeople()
g.score = 9999
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
print('-----------------------------------------\n')


#使用@property////////////////////////////////////////
#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
s = Student()
s.score = 9999
#这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
class Student(object):
    def get_score(self):
         return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print('s.score =', s.score) # OK，实际转化为s.get_score()
s.score = 9999
#注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2015 - self._birth
#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
print('-----------------------------------------\n')


#多重继承////////////////////////////////////////////
