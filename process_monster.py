import os 
import subprocess
import multiprocessing
import psutil
import time

# 2021 Currently Under Construction - Doesn't work - Trevor Knight - Under Development

def startProcess(name, path):
    """
    Starts a process in the background and writes a PID file

    returns integer: pid
    """


    # Start process
    process = subprocess.Popen(path + ' > /dev/null 2> /dev/null &', shell=True)

    # Write PID file
    pidfile = open("processes.txt", 'w')
    pidfile.write(str(process.pid))
    pidfile.close()

    return process.pid


id = startProcess("notepad", "/mnt/c/Windows/notepad.exe")

def window_id(proc_id):
    proc = subprocess.Popen(['wmctrl', '-lp'],
                            env=os.environ,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    out = proc.communicate()[0]
    for l in out.split('\n'):
        s = l.strip().split()
        if len(s) > 1 and int(s[2]) == proc_id:
            return s[0]

def wait_for_window(proc_id, timeout=15):
    wid = None
    poll_interval = 1
    attempts = max(1, timeout // poll_interval)
    while wid is None and attempts > 0:
        attempts -= 1
        wid = window_id(proc_id)
        if wid is None:
            proc = psutil.Process(proc_id)
            for child_proc in proc.children(recursive=True):
                wid = window_id(child_proc.pid)
                if wid is not None:
                    break
        if wid is None:
            time.sleep(poll_interval)
    print(wid)
    return wid


def resize_window(pid, geometry):
    wid = wait_for_window(pid)
    if wid is None:
        print("no")
    else:
        cmd = ['wmctrl', '-i', '-r', wid, '-e', geometry]
        subprocess.Popen(cmd, env=os.environ)


wait_for_window(id)