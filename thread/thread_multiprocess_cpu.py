from multiprocessing import Process, Queue
from datetime import datetime

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return


if __name__ == "__main__":
    start_time = datetime.now()

    START, END = 0, 50000000
    result = Queue()
    th1 = Process(target=work, args=(1, START, END // 3, result))
    th2 = Process(target=work, args=(2, END // 2, END, result))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    print(f"Result: {total}")

    time_elapsed = datetime.now() - start_time
    print(f'걸린시간 : {time_elapsed}')