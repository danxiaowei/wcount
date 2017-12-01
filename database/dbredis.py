#!/usr/local/bin/pyton
#!encoding:utf8

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import redis

def hello(request):
    str=redis.__file__
    str+="<br>"
    r = redis.Redis(host='192.168.8.212',port=6379,db=0)
    info = r.info()
    str+=("Set Hi <br>")
    r.set('Hi','HelloWorld-APP1')
    str+=("Get Hi:%s <br>" % r.get('Hi'))
    str+=("Redis Info: <br>")
    str+=("Key: Info Value")
    for key in info:
        str+=("%s: %s <br>" % (key,info[key]))
    return HttpResponse(str)

r = redis.Redis(host='192.168.8.212', port=6379, db= 0)
r.set('address','bj')
print r.get('address')




import re


def foo(xpath, content):
    print xpath
    if xpath.startswith('/'):
        arr= xpath[1:].split('/', 1)
        node = arr[0]
        c = re.compile(r"\<%s\>(.*?)\<\/%s\>" % (node, node), re.S)
        # print c.pattern
        content_list = c.findall(content)
        if len(arr) > 1:
            xpath = '/' + arr[1]
            return foo(xpath, content_list[0].strip())
        else:
            return content_list[0].strip()


s = '''<html>
        <header><title>hello world</title></header>
        <body>
            <div>
                <h1>Hello World</h1>
            </div>
            <div>
                <span>test</span>
            </div>
        </body>
        </html>'''
xpath = '/div'
print foo(xpath, s)