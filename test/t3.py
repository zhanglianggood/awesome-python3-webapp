import dict


class Student(dict):
    def __init__(self, **kw):
        super(Student, self).__init__(**kw)

    def __getattr__(self, item):
        try:
            print("__getattr__")
            return self[item]
        except KeyError:
            raise AttributeError(r"'Student' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)