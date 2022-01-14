from datetime import datetime
import os


from threading import Thread

def ping(ip_addr):
    os.system(f'ping {ip_addr} -n 5')


if __name__ == '__main__':
    start_time = datetime.now()

    ip_list = ['168.126.63.1', '168.126.63.2', '168.126.63.3', '168.126.63.4', '168.126.63.5']

    # for ip_addr in ip_list:
    #     ping(ip_addr)

    threads = []
    for ip_addr in ip_list:
        thread = Thread(target=ping, args=(ip_addr,))

        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    time_elapsed = datetime.now() - start_time
    print(f'걸린시간 : {time_elapsed}')

    print('app ended')