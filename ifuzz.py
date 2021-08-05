!#/usr/bin/env python2


import requests
import getopt 
from termcolor import colored
import sys

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
    print colored("Use: ./ifuzz.py -u http://fuzz.test.com/ -w ./wordlist.txt","red")    
    
def main():
    try:
        opts,args=getopt.getopt(sys.argv[1:],"u:w:h",["url","wordlist","help"])
    except:
        print("OOPS")
    
    url=""
    word=""
    if len(sys.argv[1:])==0:
        usage()
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-u","--url"):
            url=str(a)
        elif o in ("-w","--wordlist"):
            word=str(a)
    
    
    if url!="" and word!="":
        fuzz_url(url,word)
    elif url=="" and word!="":
        print("pls enter the url")
    elif word=="" and url!="":
        print("plz enter the wordlist")
    else:
        print ("plz enter the field")
        
def fuzz_url(u,w):
    try:
        file=open(w,"r")
    except:
        print("not a valid worlist path")
    
    words=file.readlines()
    word=list()
    for i in words:
        strn=str(i.rstrip())
        word.append(strn)
    url1=u
    for payload in word:
        requrl=url1.replace("fuzz",payload)
        res1=requests.get(requrl)
        res=requests.get(requrl).text
        if res1.status_code==200 or res1.status_code==302:
            print colored(payload ,"green"),colored("["+str(res1.status_code)+"]","green"),colored("length:","green"),colored(len(str(res)),"green"),colored(" size:","green"),colored(sys.getsizeof(res),"green")
        url1=u
    
    print colored("DONE!!!","yellow")
        
        
main()

    
