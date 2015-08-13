__author__ = 'wangcl'

from multiprocessing import Pool
import time

def f(x):
    time.sleep(1)
    return "wangcl"

def callback(x):
    print x
    print "callback"

if __name__ == '__main__':
    pool = Pool(processes=1)              # Start a worker processes.
    result = pool.apply_async(f, [10], callback=None) # Evaluate "f(10)" asynchronously calling callback when finished.
    result.wait()
    print "over"