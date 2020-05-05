# File Name: dog_cat.py


# 此类是狗的集合，此类的实例是具体的某一只狗
class Dog(object):
    def __init__(self, name):
        # Python 的私有属性用一个或两个下划线开头表示
        # 一个下划线开头的私有属性表示外部调用者不应该直接调用这个属性，但还是可以调用
        # 两个下划线外部就不能直接调用了，但也有办法
        self._name = name

    # 私有属性 _name 不可以被直接调用
    # 因此需要定义两个方法来修改和获取该属性值
    # get_name 用来获取属性值，set_name 用来修改属性值
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    # 该方法用来打印动物的叫声
    def say(self):
        # 这里 self._name 就是直接调用私有属性
        # 在类的内部可以这样写，在类的外部不可以哦
        print(self._name + 'is making sound wang wang wang...')


# 此类是猫的集合，此类的实例是具体的某一只猫
class Cat(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def say(self):
        print(self._name + 'is making sound miu miu miu...')