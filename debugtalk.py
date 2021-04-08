import time

from httprunner import __version__
import os

def get_httprunner_version():
    return __version__

def sum_two(m, n):
    return m + n

def sleep(n_secs):
    time.sleep(n_secs)

def cwd():
    return os.getcwd()

