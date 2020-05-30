# использование простых глобальных данных (не мьютексов) для определения момента
# завершения всех потоков в родительском/главном потоке; потоки совместно
# используют список, но не его элементы, при этом предполагается, что после
# создания список не будет перемещаться в памяти
import _thread as thread


stdoutmutex = thread.allocate_lock()
exitmutex = [False] * 10


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutex[myId] = True


for i in range(10):
    thread.start_new_thread(counter, (i, 100))


while False in exitmutex: pass
print('Main thread exiting')