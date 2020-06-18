def ex_decorator(fun):

    def inside():

        print('Действия до функции')
        fun()
        print('Действия после функции')

    return inside


@ex_decorator
def fun1():
    print('Я в декораторе :)')

a = fun1
# a()