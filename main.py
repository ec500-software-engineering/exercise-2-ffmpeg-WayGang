import os
import queue
import threading
import time

'''
InputFilePath = ""
OutputFilePath = ""
'''

def convert720(file):
    try:
        os.system('ffmpeg -i ' + file + ' -r 30 -b 2M -s 1280x720 ' + file + '_720.mp4')
        print('processing' + file + 'to 720P DONE')
    except Exception:
        time.sleep(1)
        print("Error1!Unable to process")

def convert480(file):
    try:
        os.system('ffmpeg -i ' + file + ' -r 30 -b 1M -s 720x480 ' + file + '_480.mp4')
        print('processing' + file + 'to 480P DONE')
    except Exception as e:
        time.sleep(1)
        print("Error2!Unable to process")

if __name__ == '__main__':
    q720 = queue.Queue()
    q480 = queue.Queue()
    thread_list = []
    num = 0
    try:
        for file in os.listdir("./"):
            if file.endswith('.mov'):
                num = num+1
                q480.put(file)
                thread_list.append(threading.Thread(target=convert480, args=(file,)))
                #print("debug1")
    except Exception:
        time.sleep(1)
        print("Error3!")
    try:
        for file in os.listdir("./"):
            if file.endswith('.mov'):
                num = num + 1
                q720.put(file)
                thread_list.append(threading.Thread(target=convert720, args=(file,)))
    except Exception:
        time.sleep(1)
        print("Error4!")

    print(str(num) + ' files in the process')

    for thread in thread_list:
        thread.start()
        #print("debug2")
 
