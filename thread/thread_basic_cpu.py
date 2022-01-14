from threading import Thread
from datetime import datetime

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return


if __name__ == "__main__":
    start_time = datetime.now()

    START, END = 0, 100000000
    result = list()

    # th1 = Thread(target=work, args=(1, START, END, result))
    #
    # th1.start()
    # th1.join()

    th1 = Thread(target=work, args=(1, START, END // 2, result))
    th2 = Thread(target=work, args=(2, END // 2, END, result))

    th1.start()
    th2.start()
    th1.join()
    th2.join()


print(f"Result: {sum(result)}")

time_elapsed = datetime.now() - start_time
print(f'걸린시간 : {time_elapsed}')