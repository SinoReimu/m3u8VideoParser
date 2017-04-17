import os
import requests


baseDir = "down/"
counter = 0

def download(url):
    r = requests.get(url) 
    with open(baseDir+str(counter)+".ts", "wb") as tsf:
         tsf.write(r.content)

m3u8 = open('1.m3u8', 'r')
mlist = []

for line in m3u8:
     if("http" in line):
         mlist.append(line)

for line in mlist:
    counter = counter + 1
    download(line)
    print("downloading file ("+str(counter+1)+"/"+str(len(mlist))+")")
