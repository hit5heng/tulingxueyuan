import threading

sum = 0
loopsum = 1000000

def myAdd():
    global sum, loopsum
    for i in range(1,loopsum):
        sum += 1

def myMinu():
    global sum, loopsum
    for i in range(1,loopsum):
        sum -= 1

if __name__ == '__main__':
    print("Starting ....{0}".format(sum))

    # 开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done .... {0}".format(sum))