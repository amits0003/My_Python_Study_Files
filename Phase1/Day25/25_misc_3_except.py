import sys
import os
import gc

try:
    f = open('noFile.txt')
except FileNotFoundError as e:
    print('custom file does not exists, error : ', e)