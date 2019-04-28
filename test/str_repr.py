# 1、创建一个Student类
class Student(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def __str__(self):
        return ("studend info: %s %s" % (self.name, self.sex))


class Student1(Student):
    def __init__(self, name, sex):
        super(Student1, self).__init__(name, sex)

    def __repr__(self):
        return ("studend info: %s %s" % (self.name, self.sex))


# 2、实例化
s = Student("wang", "man")
s1 = Student1("wang", "man")
# 3、打印实例
print(s)
print(s)
