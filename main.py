import os
import threading
import queue
import subprocess
import json

'''
InputFilePath = ""
OutputFilePath = ""
'''
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
    except Exception:
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
        # print("debug2")
'''


def v480(file, out480):

    try:
        print('-------480p processing-------')
        subprocess.call(['ffmpeg',
                         '-i', file,
                         '-r', '30',
                         '-b:v', '2M',
                         '-s', 'hd480',
                         '-loglevel', 'quiet',
                         out480])
        print('-------480p done!-------')
    except Exception:
        print(Exception)

def v720(file, out720):

    try:
        print('-------720p processing-------')
        subprocess.call(['ffmpeg',
                         '-i', file,
                         '-r', '30',
                         '-b:v', '2M',
                         '-s', 'hd720',
                         '-loglevel', 'quiet',
                         out720])
        print('-------720p done!-------')
    except Exception:
        print(Exception)


def ffprobe(file):
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                    str(file)],text=True)
    #meta = meta.decode("utf-8")
    return json.loads(meta)


def thread():
    q = queue.Queue()
    thread_list = []
    filenums = 0
    try:
        for file in os.listdir("./"):
            format = file.split('.')
            if format[-1] == 'mov':
                out720 = format[0] + '_720p.' + format[-1]
                out480 = format[0] + '_480p.' + format[-1]
                q.put(file)
                thread_list.append(threading.Thread(target=v480, args=(file, out480)))
                thread_list.append(threading.Thread(target=v720, args=(file, out720)))
                filenums = filenums + 1

    except Exception:
        print(Exception)

    print(str(filenums) + ' files in total')
    for thread in thread_list:
        thread.start()

if __name__ == '__main__':
    thread()
