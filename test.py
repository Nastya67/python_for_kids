from multiprocessing import Process as proc

def f():
    exec("while True:\n\tprint(0)")

import psutil, time
import subprocess
subp = subprocess.Popen(['progname'])

p = psutil.Process(subp.pid)
try:
    p.wait(timeout=60*60)
except psutil.TimeoutExpired:
    p.kill()
    raise
