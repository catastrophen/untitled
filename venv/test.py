import sys
import urllib
import urllib.error
import urllib.request

url=sys.argv[1]      #命令行参数
try:
    info=urllib.request.urlopen(url).info()
    print(info)
except urllib.error.URLError as e:
    print(e)