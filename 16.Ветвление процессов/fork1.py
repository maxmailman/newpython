# ответвляет дочерние процессы, пока не будет нажата клавиша ‘q’
# код для Unix систем
import os


def child():
    print('Hello from child', os.getpid())
    os._exit(0)  # иначе произодет возврат в родительский цикл


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break


parent()
