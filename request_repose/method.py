"""
常用的几种方法
静态方法、实例方法、类方法
静态方法在方法 前+@staticmethod
静态方法中无法使用实例方法和属性

实例方法
实例方法入参第一个值默认是self，不建议使用其他关键字进行替换----只当前调用的对象。实例方法只能用实例对象进行调用

类方法
类方法和静态方法类似，需要使用@classmethod关键字进行修饰，且方法入参第一个值默认为cls。类方法可以通过类对象和实例对象调用
类方法调用在实例对象初始化之前。如果实现功能时需要在初始化之前做一些校验的工作时可以使用此方法
例：在进行文件读写时，先检查文件时候被打开

"""
class testFunction():
    classA = 'aaaaaa'
    def __init__(self):
        """
        这是一个构造函数
        """
        pass
    def example(self, exname):
        exname = self.exname
        print("实例方法被调用")
    @staticmethod
    def testStatic():
        print("静态方法被调用")
    @classmethod
    def testClass(cls):
        print("类方法被调用")
if __name__ == '__main__':
    #实例化类
    test1 = testFunction()
    print(test1.classA)
    test1.testStatic()
    test1.testClass()
    #test1.example('self')

