import time
sec = int(input("Enter the time in seconds -> "))

def ct(sec):
    while sec > 0:

        mins = int(sec/60)
        secs = int(sec%60)

        timer = f'{mins} : {secs}'
        print(timer, end = '\r')
        time.sleep(1)
        sec -= 1

    print("Time's up")

ct(sec)
