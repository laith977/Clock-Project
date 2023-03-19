import time


def enter_timer():
    x = input("Enter Time in this context hr/min/sec")
    return x


def create_mylist(x):
    z = x.split('/')
    return z


def output_timer(arr):
    hrr = int(arr[0])
    minn = int(arr[1])
    sec = int(arr[2])
    while hrr or minn or sec:

        if sec == -1:
            minn = minn - 1
            sec = 59
        if minn == -1:
            minn = 59
            hrr = hrr - 1
        print(f'{hrr if hrr > 9 else "0" + str(hrr)}:{minn if minn > 9 else "0" + str(minn)}:'
              f'{sec if sec > 9 else "0"+str(sec)}')
        sec = sec - 1
        time.sleep(1)


timerr = enter_timer()
timer = create_mylist(timerr)
output_timer(timer)
