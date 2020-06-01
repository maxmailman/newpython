# взаимодействие потоков производителей и потребителей посредством очереди

numconsumers = 2    # Количество потоков потребителей
numproducers = 4    # КОличество потоков производителей
nummessage = 4      # Количество сообщений, помещаемых производителем


import _thread as thread, queue, time


safeprint = thread.allocate_lock()

dataQueue = queue.Queue()

def producer(idnum):
    for msgnum in range(nummessage):
        time.sleep(idnum)
        dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))

def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safeprint:
                print('consumer', idnum, 'got =>', data)

if __name__ == '__main__':
    for i in range(numconsumers):
        thread.start_new_thread(consumer, (i, ))
    for i in range(numproducers):
        thread.start_new_thread(producer, (i, ))
    time.sleep(((numproducers-1) * nummessage) + 1)
    print('Main thread exit.')