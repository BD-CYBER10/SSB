#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/3017062245271082/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sarfraz.so Sarfraz32.so')
except:
    pass
os.system('rm -rf Sarfraz.so Sarfraz32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Sarfraz.so'):
        os.system('curl -L https://raw.githubusercontent.com/adnanvau4/ss/main/Approval.txt') 
        import Sarfraz
    else:
        import Sarfraz

elif bit == '32bit':
    if not os.path.isfile('Sarfraz32.so'):
        os.system('curl -L https://raw.githubusercontent.com/adnanvau4/SSB/main/Approval.txt') 
        import Sarfraz32
    else:
        import Sarfraz32
