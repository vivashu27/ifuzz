#!/usr/bin/env python


import requests
import getopt 
from termcolor import colored
import sys
import re

cookie=""
def usage():
    print colored("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n","red")
    print colored(''' 
                      _  __
                     (_)/ _|_   _ ________
                     | | |_| | | |_  /_  /
                     | |  _| |_| |/ / / / 
                     |_|_|  \__,_/___/___|\n\n\n''',"yellow")
    print colored("\t\t\tby @luffy27\n\n","yellow")
    print colored(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n","red")
    print colored("-h --help for help\n","red")
    print colored("-u --url for url to test\n","red")
    print colored("-w --wordlist for wordlist used for fuzzing\n","red")
    print colored("-x --post for POST API method used for fuzzing\n","red")
    print colored("-d --data for data parameter used for fuzzing(use with -x)\n","red")
    print colored("-c --cookie to be used\n","red")
    print colored("Use: ./ifuzz.py -u http://fuzz.test.com/ -w ./wordlist.txt\n","red")    
    print colored("Use: ./ifuzz.py -u http://test.com/ -w wordlist.txt -x POST -d param -c <cookiename:value>\n","red")
    
def main():
    try:
        opts,args=getopt.getopt(sys.argv[1:],"u:w:x:d:c:h",["url","wordlist","post","data","cookie","help"])
    except:
        print("OOPS")
    
    url=""
    word=""
    post=False
    param=""
    global cookie
    if len(sys.argv[1:])==0:
        usage()
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-u","--url"):
            url=str(a)
        elif o in ("-w","--wordlist"):
            word=str(a)
        elif o in ("-w","--wordlist"):
            word=str(a)
        elif o in ("-x","--post"):
            post=True
        elif o in ("-d","--data"):
            param=str(a)
        elif o in ("-c","--cookie"):
            cookie=str(a)
    
    
    if url!="" and word!="" and not post and param=="":
        fuzz_url(url,word)
    elif url=="" and word!="":
        print("pls enter the url")
    elif word=="" and url!="":
        print("plz enter the wordlist")
    elif not re.findall("fuzz",url) and post and param!="" and url!="" and word!="":
        fuzz_url_param(url,word,param)
    else:
        print ("plz enter the field properly")
        
def fuzz_url(u,w):
    try:
        file=open(w,"r")
    except:
        print("not a valid worlist path")
    
    word=list()
    word=re.split("\n",file.read())
    url1=u
    if cookie =="":
        for payload in word:
            requrl=url1.replace("fuzz",payload)
            res1=requests.get(requrl)
            res=requests.get(requrl).text
            if res1.status_code==200 or res1.status_code==302:
                print colored(payload ,"green"),colored("["+str(res1.status_code)+"]","green"),colored("length:","green"),colored(len(str(res)),"green"),colored(" size:","green"),colored(sys.getsizeof(res),"green")
            url1=u

    if cookie !="":
        cok_name,value=re.split(":",cookie)
        for payload in word:
            requrl=url1.replace("fuzz",payload)
            res1=requests.get(requrl,headers={"Cookie":cok_name+"="+value})
            res=res1.text
            if res1.status_code==200 or res1.status_code==302:
                print colored(payload ,"green"),colored("["+str(res1.status_code)+"]","green"),colored("length:","green"),colored(len(str(res)),"green"),colored(" size:","green"),colored(sys.getsizeof(res),"green")
            url1=u
        
    print colored("DONE!!!","yellow")

def fuzz_url_param(u,w,p):
    try:
        file=open(w,"r")
    except:
        print("not a valid worlist path")
    
    word=list()
    word=re.split("\n",file.read())
    url1=u
    if cookie =="":
        for payload in word:
            res1=requests.post(u,data={p:payload})
            res=res1.text
            if res1.status_code==200 or res1.status_code==302:
                print colored(payload ,"green"),colored("["+str(res1.status_code)+"]","green"),colored("length:","green"),colored(len(str(res)),"green"),colored(" size:","green"),colored(sys.getsizeof(res),"green")
            url1=u

    if cookie !="":
        cok_name,value=re.split(":",cookie)
        for payload in word:
            res1=requests.post(u,data={p:payload},headers={"Cookie":cok_name+"="+value})
            res=res1.text
            if res1.status_code==200 or res1.status_code==302:
                print colored(payload ,"green"),colored("["+str(res1.status_code)+"]","green"),colored("length:","green"),colored(len(str(res)),"green"),colored(" size:","green"),colored(sys.getsizeof(res),"green")
            url1=u
    
    print colored("DONE!!!","yellow")
        
        
main()

    
