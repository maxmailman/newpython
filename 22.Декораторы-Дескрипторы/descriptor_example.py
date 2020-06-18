# class Foo:
#     def __init__(self):
#         self.bar = 'Привет!'
#
#
# foo = Foo()
# print(foo.bar)
# print(foo.__dict__)
# print(foo.__dict__['bar'])

class Foo:
    def __init__(self):
        self.bar = 'Привет!'

    def __getattr__(self, item):
        return 'Пока!'

foo = Foo()
print(foo.bar)
print(foo.trt)
print(foo.__dict__)